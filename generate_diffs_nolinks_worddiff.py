#!/usr/bin/env python3

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE_REPO = Path("/Users/jpradocueva/Documents/github/focus/FOCUS_Spec")
TARGET_REPO = Path("/Users/jpradocueva/Documents/github/focus/focus_extraction_test")

# Separate location for the input file that lists target markdown files
COMMAND_REPO = Path("/Users/jpradocueva/Documents/github/focus/focus_extraction_test")
INPUT_FILE = COMMAND_REPO / "diff_target_files.md"

# Comparison direction
DIFF_FROM_REF = "v1.3"
DIFF_TO_REF = "working_draft"

OUTPUT_DIRS = {
    "ATT": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT",
    "CCT": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CCT",
    "CAU": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CAU",
}

WORD_DIFF_REGEX = r"[^[:space:]]+"

# Strip Markdown links but keep the visible label text:
# [Label](target) -> Label
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate detailed diff output files for a single section from diff_target_files.md."
    )
    parser.add_argument(
        "section",
        choices=sorted(OUTPUT_DIRS.keys()),
        help="Section to process: ATT, CCT, or CAU",
    )
    return parser.parse_args()


def extract_section_paths(file_path: Path, section: str) -> list[str]:
    lines = file_path.read_text(encoding="utf-8").splitlines()
    target_header = f"### {section}"
    in_section = False
    paths: list[str] = []

    for raw_line in lines:
        line = raw_line.strip()

        if line == target_header:
            in_section = True
            continue

        if in_section and line.startswith("### "):
            break

        if not in_section:
            continue

        # Skip blank lines and markdown comments/headings that are not file paths
        if not line or line.startswith("#"):
            continue

        paths.append(line)

    if not paths:
        raise ValueError(f"No file paths found for section {section} in {file_path}")

    return paths


def build_output_path(section: str, spec_path: str) -> Path:
    filename = Path(spec_path).stem
    output_name = f"{filename}_diff_1-3-working-draft.md"
    return OUTPUT_DIRS[section] / output_name


def fetch_file_from_ref(repo: Path, git_ref: str, spec_path: str) -> tuple[bool, str]:
    """
    Returns:
      (True, content)  -> file exists in ref
      (False, "")      -> file does not exist in ref
    Raises:
      RuntimeError     -> unexpected git error
    """
    cmd = ["git", "show", f"{git_ref}:{spec_path}"]
    result = subprocess.run(
        cmd,
        cwd=repo,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    if result.returncode == 0:
        return True, result.stdout

    stderr = (result.stderr or "").strip()
    stdout = (result.stdout or "").strip()
    combined = f"{stderr}\n{stdout}".strip()

    not_found_markers = (
        "exists on disk, but not in",
        "pathspec",
        "does not exist in",
        "fatal: path",
    )

    if any(marker in combined for marker in not_found_markers):
        return False, ""

    raise RuntimeError(
        f"git show failed for {git_ref}:{spec_path} "
        f"(exit {result.returncode}): {combined or 'unknown error'}"
    )


def strip_markdown_links(content: str) -> str:
    return MARKDOWN_LINK_RE.sub(r"\1", content)


def write_temp_content(content: str, suffix: str) -> str:
    tmp = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=suffix,
        prefix="focus_diff_",
        delete=False,
    )
    try:
        tmp.write(content)
        tmp.flush()
        return tmp.name
    finally:
        tmp.close()


def run_detailed_diff(
    from_label: str,
    to_label: str,
    from_file: str,
    to_file: str,
) -> tuple[bool, str]:
    """
    Returns:
      (True, diff_output) on success, including the case where files differ
      (False, error_text) on real execution failure
    """
    cmd = [
        "git",
        "diff",
        "--no-index",
        "--word-diff=plain",
        f"--word-diff-regex={WORD_DIFF_REGEX}",
        from_file,
        to_file,
    ]

    result = subprocess.run(
        cmd,
        cwd=SOURCE_REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    # git diff returns:
    # 0 -> no differences
    # 1 -> differences found
    # >1 -> error
    if result.returncode in (0, 1):
        return True, result.stdout

    error_text = result.stderr.strip() or result.stdout.strip() or f"git diff failed with exit code {result.returncode}"
    return False, error_text


def write_output_file(output_path: Path, content: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"## Diff\n\n{content}", encoding="utf-8")


def format_missing_both_error(spec_path: str) -> str:
    return (
        f"ERROR: File not found in either comparison ref.\n\n"
        f"- Path: `{spec_path}`\n"
        f"- From ref: `{DIFF_FROM_REF}`\n"
        f"- To ref: `{DIFF_TO_REF}`\n"
    )


def main() -> int:
    args = parse_args()
    section = args.section

    try:
        spec_paths = extract_section_paths(INPUT_FILE, section)
    except FileNotFoundError:
        print(f"ERROR: Input file not found: {INPUT_FILE}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    OUTPUT_DIRS[section].mkdir(parents=True, exist_ok=True)

    files_generated = 0
    failures = 0

    for spec_path in spec_paths:
        output_path = build_output_path(section, spec_path)

        try:
            from_exists, from_content = fetch_file_from_ref(SOURCE_REPO, DIFF_FROM_REF, spec_path)
            to_exists, to_content = fetch_file_from_ref(SOURCE_REPO, DIFF_TO_REF, spec_path)
        except RuntimeError as exc:
            failures += 1
            write_output_file(output_path, f"ERROR: {exc}\n")
            files_generated += 1
            print(f"Processed with error: {output_path.name}")
            continue

        if not from_exists and not to_exists:
            failures += 1
            write_output_file(output_path, format_missing_both_error(spec_path))
            files_generated += 1
            print(f"Processed with error: {output_path.name}")
            continue

        from_processed = strip_markdown_links(from_content)
        to_processed = strip_markdown_links(to_content)

        from_temp = write_temp_content(from_processed, "_from.md")
        to_temp = write_temp_content(to_processed, "_to.md")

        from_label = f"{DIFF_FROM_REF}:{spec_path}"
        to_label = f"{DIFF_TO_REF}:{spec_path}"

        success, diff_output = run_detailed_diff(
            from_label=from_label,
            to_label=to_label,
            from_file=from_temp,
            to_file=to_temp,
        )

        if not success:
            failures += 1
            write_output_file(output_path, f"ERROR: {diff_output}\n")
        else:
            if not diff_output.strip():
                diff_output = "No differences found.\n"
            write_output_file(output_path, diff_output)

        files_generated += 1
        print(f"Processed: {output_path.name}")

    print(f"section processed: {section}")
    print(f"number of file paths found: {len(spec_paths)}")
    print(f"number of files generated: {files_generated}")
    print(f"number of failures: {failures}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
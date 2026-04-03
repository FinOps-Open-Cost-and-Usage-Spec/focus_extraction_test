#!/usr/bin/env python3

import argparse
import shlex
import subprocess
import sys
from pathlib import Path


SOURCE_REPO = Path("/Users/jpradocueva/Documents/github/focus/FOCUS_Spec")
TARGET_REPO = Path("/Users/jpradocueva/Documents/github/focus/FOCUS_Spec")
INPUT_FILE = TARGET_REPO / "diff_command.md"

OUTPUT_DIRS = {
    "ATT": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT",
    "CCT": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CCT",
    "CAU": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CAU",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate diff output files for a single section from diff_command.md."
    )
    parser.add_argument(
        "section",
        choices=sorted(OUTPUT_DIRS.keys()),
        help="Section to process: ATT, CCT, or CAU",
    )
    return parser.parse_args()


def extract_section_commands(file_path: Path, section: str) -> list[str]:
    lines = file_path.read_text(encoding="utf-8").splitlines()
    target_header = f"### {section}"
    in_section = False
    commands: list[str] = []

    for raw_line in lines:
        line = raw_line.strip()

        if line == target_header:
            in_section = True
            continue

        if in_section and line.startswith("### "):
            break

        if in_section and line:
            commands.append(line)

    if not commands:
        raise ValueError(f"No commands found for section {section} in {file_path}")

    return commands


def extract_spec_path(command: str) -> str:
    parts = shlex.split(command)
    for part in reversed(parts):
        if part.startswith("specification/") and part.endswith(".md"):
            return part
    raise ValueError(f"Could not find specification markdown path in command: {command}")


def build_output_path(section: str, spec_path: str) -> Path:
    filename = Path(spec_path).stem
    output_name = f"{filename}_diff_1-3-working-draft.md"
    return OUTPUT_DIRS[section] / output_name


def run_git_diff(command: str) -> tuple[bool, str]:
    try:
        parts = shlex.split(command)
    except ValueError as exc:
        return False, str(exc)

    try:
        result = subprocess.run(
            parts,
            cwd=SOURCE_REPO,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError as exc:
        return False, str(exc)

    if result.returncode != 0:
        error_text = result.stderr.strip() or result.stdout.strip() or f"git diff failed with exit code {result.returncode}"
        return False, error_text

    return True, result.stdout


def write_output_file(output_path: Path, content: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"## Diff\n\n{content}", encoding="utf-8")


def main() -> int:
    args = parse_args()
    section = args.section

    try:
        commands = extract_section_commands(INPUT_FILE, section)
    except FileNotFoundError:
        print(f"ERROR: Input file not found: {INPUT_FILE}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    OUTPUT_DIRS[section].mkdir(parents=True, exist_ok=True)

    files_generated = 0
    failures = 0
    unparsed_counter = 0

    for command in commands:
        try:
            spec_path = extract_spec_path(command)
            output_path = build_output_path(section, spec_path)
        except ValueError as exc:
            failures += 1
            files_generated += 1
            unparsed_counter += 1
            fallback_name = f"unparsed_{unparsed_counter}_diff_1-3-working-draft.md"
            output_path = OUTPUT_DIRS[section] / fallback_name
            write_output_file(output_path, f"ERROR: {exc}")
            continue

        success, output = run_git_diff(command)
        if not success:
            failures += 1
            write_output_file(output_path, f"ERROR: {output}")
        else:
            write_output_file(output_path, output)

        files_generated += 1
        print(f"Processed: {output_path.name}")

    print(f"section processed: {section}")
    print(f"number of commands found: {len(commands)}")
    print(f"number of files generated: {files_generated}")
    print(f"number of failures: {failures}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
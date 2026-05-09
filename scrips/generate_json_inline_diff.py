# ============================================================
# Generate inline diff
# Ignore indentation-only changes
# ============================================================

output_lines = []

for line in difflib.ndiff(old_text, new_text):

    if line.startswith("- "):
        content = line[2:]
        stripped = content.lstrip()

        # Skip removed lines caused only by indentation changes
        if stripped in [l.lstrip() for l in new_text]:
            continue

        output_lines.append(f"[-{content}-]")

    elif line.startswith("+ "):
        content = line[2:]
        stripped = content.lstrip()

        # Skip added lines caused only by indentation changes
        if stripped in [l.lstrip() for l in old_text]:
            continue

        output_lines.append(f"{{+{content}+}}")

    elif line.startswith("  "):
        output_lines.append(line[2:])
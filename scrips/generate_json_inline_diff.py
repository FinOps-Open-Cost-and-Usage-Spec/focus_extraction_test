#!/usr/bin/env python3

import json
import difflib
from pathlib import Path

# ============================================================
# JSON INLINE DIFF GENERATOR
# ============================================================
# Produces inline diffs using:
#   [-removed content-]
#   {+added content+}
#
# Designed for comparing normalized JSON artifacts
# in the FOCUS requirements model workflows.
# ============================================================

# Input files
old_file = Path(
    "specification/requirements_model/releases/1.4/model_rules/attributes/deliveryhandling.json"
)

new_file = Path(
    "specification/requirements_model/releases/1.4/extraction_artifacts/specification/attributes/delivery_handling_ph3.json"
)

# Output file
output_file = Path(
    "specification/requirements_model/releases/1.4/extraction_artifacts/diff-working_draft-2344/delivery_handling_diff_working_draft-2344.json"
)

# ============================================================
# Ensure output directory exists
# ============================================================

output_file.parent.mkdir(parents=True, exist_ok=True)

# ============================================================
# Load and normalize JSON
# ============================================================

old_text = json.dumps(
    json.loads(old_file.read_text()),
    indent=2,
    sort_keys=True
).splitlines()

new_text = json.dumps(
    json.loads(new_file.read_text()),
    indent=2,
    sort_keys=True
).splitlines()

# ============================================================
# Generate inline diff
# ============================================================

output_lines = []

for line in difflib.ndiff(old_text, new_text):

    # Removed line
    if line.startswith("- "):
        output_lines.append(f"[-{line[2:]}-]")

    # Added line
    elif line.startswith("+ "):
        output_lines.append(f"{{+{line[2:]}+}}")

    # Unchanged line
    elif line.startswith("  "):
        output_lines.append(line[2:])

# ============================================================
# Write output
# ============================================================

output_file.write_text("\n".join(output_lines))

print("")
print("============================================")
print(" JSON inline diff generated successfully")
print("============================================")
print(f"Old file : {old_file}")
print(f"New file : {new_file}")
print(f"Output   : {output_file}")
print("============================================")
print("")
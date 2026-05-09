## JSON Inline Diff Generator

This script generates an inline diff between two normalized JSON files.

The output highlights changes using the following format:

- Removed content:
  ```text
  [-old content-]
  ```

- Added content:
  ```text
  {+new content+}
  ```

The generated diff file is written into the `FOCUS_Spec` repository under the configured extraction artifacts directory.

---

### Prerequisites

Install `jq`:

```bash
brew install jq
```

Verify installation:

```bash
jq --version
```

---

### How to Run

From the `FOCUS_Spec` repository root:

```bash
cd /Users/jpradocueva/Documents/github/focus/FOCUS_Spec
```

Run the script:

```bash
python3 /Users/jpradocueva/Documents/github/focus/focus_extraction_test/scrips/generate_json_inline_diff.py
```

---

### Expected Output

The script will:

1. Load and normalize the two JSON files
2. Ignore indentation-only changes
3. Compare meaningful line-level content changes
4. Generate inline delta markers
5. Write the diff output to:

```text
specification/requirements_model/releases/1.4/extraction_artifacts/diff-working_draft-2344/delivery_handling_diff_working_draft-2344.json
```

---

### Notes

- The script must be executed from inside the `FOCUS_Spec` repository root.
- The script itself can be stored outside the production repository.
- Output directories are automatically created if they do not exist.

### Note About Indentation Handling

The script ignores indentation-only differences between the two JSON files.

This is useful when one JSON file has the same content but is nested differently or formatted with different spacing. The diff output focuses on meaningful content changes, such as:

- Added or removed fields
- Changed values
- Changed rule IDs
- Changed dependencies
- Added or removed model rules

Indentation-only changes are not reported in the output.

## Important Limitation

The script compares normalized JSON line-by-line. It reduces formatting noise, but it is not a full semantic JSON diff tool. If a rule is renamed, moved, or restructured, the output may still show larger blocks of additions and removals.
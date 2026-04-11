# focus_extraction_test
This repository is dedicated to extract normative requirements. It is used for testing, you should ignore its content.


## Recommended Execution Order

1. Navigate to the target repository:

```bash
cd /Users/jpradocueva/Documents/github/focus/focus_extraction_test
```

2. Verify that the input file exists:

```bash
ls diff_command.md
```

3. Run a small test using the ATT section:

```bash
python3 generate_diffs.py ATT
```

4. Review the generated output files in:

```bash
specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT/
```

5. If the ATT output is correct, process the CCT section:

```bash
python3 generate_diffs.py CCT
```

6. Finally, process the CAU section (largest set):

```bash
python3 generate_diffs.py CAU
```

7. Review outputs in their respective directories:

```bash
ATT:

specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT/

CCT:

specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CCT/

CAU:

specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CAU/
```

## Configuration

Before running the script, ensure the following configuration values are correctly set in `generate_diffs_nolinks_worddiff.py`.

These constants define where files are read from, how comparisons are performed, and where outputs are written.

### Repository Paths

```python
SOURCE_REPO = Path("/Users/jpradocueva/Documents/github/focus/FOCUS_Spec")
TARGET_REPO = Path("/Users/jpradocueva/Documents/github/focus/FOCUS_Spec")
```

* **SOURCE_REPO:** Repository used to read file contents and run `git` commands.
* **TARGET_REPO:** Repository where the generated diff output files will be written.
* These can be the same repository or different ones depending on your workflow.

### Input File Location

```python
COMMAND_REPO = Path("/Users/jpradocueva/Documents/github/focus/focus_extraction_test")
INPUT_FILE = COMMAND_REPO / "diff_target_files.md"
```

* **COMMAND_REPO:** Location of the file that lists the markdown files to compare.
* **INPUT_FILE:** The file containing grouped file paths (ATT, CCT, CAU).
* Ensure `diff_target_files.md` exists and is correctly populated before running the script.

### Branch Comparison

```python
DIFF_FROM_REF = "v1.3"
DIFF_TO_REF = "working_draft"
```

* Defines the direction of the comparison:
    * **DIFF_FROM_REF:** Base version (e.g., released version)
    * **DIFF_TO_REF:** Target version (e.g., working branch)
* The script will compute diffs as: `FROM → TO`

### Output Directories

```python
OUTPUT_DIRS = {
    "ATT": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT",
    "CCT": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CCT",
    "CAU": TARGET_REPO / "specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CAU",
}
```

* Defines where the generated diff files will be stored for each section:
* **ATT, CCT, CAU**
* The script will automatically create these directories if they do not exist.
* Output files follow the naming pattern:

```bash
<filename>_diff_1-3-working-draft.md
```

### Summary

Before running the script, verify:

*Paths to repositories are correct
* `diff_target_files.md` exists and is populated
* Branch names (`DIFF_FROM_REF`, `DIFF_TO_REF`) are valid in the source repo
* Output directories are aligned with your desired location

Incorrect configuration may result in missing files, empty diffs, or execution errors.


## Detailed Diff (No Links, Word-Level)

This mode generates **review-friendly diffs** by removing Markdown links and using inline word-level markers (`[-old-]{+new+}`) to make changes easier to read.

1. Verify that the input file with target paths exists:

```bash
ls diff_target_files.md
```

2. Run a small test using the ATT section:

```bash
python3 generate_diffs_nolinks_worddiff.py ATT
```

3. Review the generated output files in:

specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT/

4. If the ATT output is correct, process the CCT section:

```bash
python3 generate_diffs_nolinks_worddiff.py CCT
```

5. Finally, process the CAU section (largest set):

```bash
python3 generate_diffs_nolinks_worddiff.py CAU
```

6. Review outputs in their respective directories:

> ATT:
>
> specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT/
>
> CCT:
>
> specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CCT/
>
> CAU:
>
> specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CAU/


## Diff Command 
* Provides a diff command with color (command line) for each file.
* Deltas with [-deleted-]{+added+} format for easy review.
* Does not include links in the diff output.


```bash
git show v1.3:specification/datasets/cost_and_usage/columns/allocatedtags.md \
  | perl -pe 's/\[([^\]]+)\]\([^)]+\)/$1/g' \
  > /tmp/allocatedtags_v13.md && \

git show working_draft:specification/datasets/cost_and_usage/columns/allocatedtags.md \
  | perl -pe 's/\[([^\]]+)\]\([^)]+\)/$1/g' \
  > /tmp/allocatedtags_working.md && \

git diff --no-index \
  --color \
  --word-diff=plain \
  --word-diff-regex='[^[:space:]]+' \
  /tmp/allocatedtags_v13.md /tmp/allocatedtags_working.md
  ``` 
  Other example commands can be found in the `diff_commands.md` file.:

  ```bash
git show v1.3:specification/datasets/cost_and_usage/columns/contractapplied.md \
  | perl -pe 's/\[([^\]]+)\]\([^)]+\)/$1/g' \
  > /tmp/contractapplied_v13.md && \

git show working_draft:specification/datasets/cost_and_usage/columns/contractapplied.md \
  | perl -pe 's/\[([^\]]+)\]\([^)]+\)/$1/g' \
  > /tmp/contractapplied_working.md && \

git diff --no-index \
  --color \
  --word-diff=plain \
  --word-diff-regex='[^[:space:]]+' \
  /tmp/contractapplied_v13.md /tmp/contractapplied_working.md
  ``` 

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


## Detailed Diff (No Links, Word-Level)

This mode generates **review-friendly diffs** by removing Markdown links and using inline word-level markers (`[-old-]{+new+}`) to make changes easier to read.

1. Verify that the input file with target paths exists:

```bash
ls diff_target_files.md
```

2. Run a small test using the ATT section:

```bash
python generate_diffs_nolinks_worddiff.py ATT
```

3. Review the generated output files in:

specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT/

4. If the ATT output is correct, process the CCT section:

```bash
python generate_diffs_nolinks_worddiff.py CCT
```

5. Finally, process the CAU section (largest set):

```bash
python generate_diffs_nolinks_worddiff.py CAU
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


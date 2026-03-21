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
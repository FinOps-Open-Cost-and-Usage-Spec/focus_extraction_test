Write a complete Python script. Do not explain. Only output the final code.

Create a script that reads the file `diff_command.md` from the root of the repository `focus_extraction_test` and generates diff output files for one section at a time.

### Repositories
- Source repository (read-only, used to run git commands):
  `/Users/jpradocueva/Documents/github/focus/FOCUS_Spec`
- Target repository (write-only, used to read diff_command.md and write output files):
  `/Users/jpradocueva/Documents/github/focus/focus_extraction_test`

### Input file
- `/Users/jpradocueva/Documents/github/focus/focus_extraction_test/diff_command.md`

### Input format
The file contains sections with these headers:
- `### ATT`
- `### CCT`
- `### CAU`

Under each section are full git diff commands already populated, for example:
`git diff --word-diff v1.3 working_draft -- specification/attributes/column_handling.md`

### Script requirements
- Accept one input argument: `ATT`, `CCT`, or `CAU`
- Only process commands under the requested section
- Ignore all other sections
- Execute git commands from:
  `/Users/jpradocueva/Documents/github/focus/FOCUS_Spec`
- Do not modify files in the source repository
- Write output files only in the target repository

### Output directories
- ATT:
  `specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/ATT/`
- CCT:
  `specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CCT/`
- CAU:
  `specification/requirements_model/releases/1.4/extraction_artifacts/diff-1_3-vs-working_draft/CAU/`

### Output filename rule
For each command, extract the markdown filename from the specification path.
Example:
- path: `specification/attributes/column_handling.md`
- output file: `column_handling_diff_1-3-working-draft.md`

### Output file content
Each output file must contain exactly:

## Diff

<full git diff output>

### Additional requirements
- Create output directories if they do not exist
- Preserve the exact diff output
- Use UTF-8 when writing files
- If a command fails, still create the output file with:

## Diff

ERROR: <error message>

- Print a summary at the end showing:
  - section processed
  - number of commands found
  - number of files generated
  - number of failures

Please generate the script in Python.
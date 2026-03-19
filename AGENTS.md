# Update Data Agent

Fetch website content and update dataset files.

## Instructions

- The input month will be in the format `YYYY-MM`.
- Map the month to the corresponding URL using `README.md`.
- Fetch the webpage (static HTML only, no JS execution).
- Extract data from the main table on the page.

## Data Update Rules

- Update as needed:
  - `data/monthly-cases.csv`
  - `data/monthly-deaths.csv`
  - `data/yearly-cases.csv`
  - `data/yearly-deaths.csv`
- If the month already exists → update the row
- If not → append a new row
- Keep rows sorted by date (ascending)
- Do NOT:
  - change column order
  - introduce new columns
  - write non-numeric values into numeric fields

## Validation

- If the website contains columns not present in CSV → STOP and report
- If required columns are missing in CSV → STOP and report
- If fetching/parsing fails → STOP and report

## Execution Constraints

- Do NOT write or run custom scripts (Python, Bash, etc.)
- You MAY use the `runTests` tool

## Final Step

- Run tests using `runTests` with `check.py` (`python3 -m unittest -v check`)

## Output

Report:

1. Files updated
2. Rows added/modified
3. Test results

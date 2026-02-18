# Agents

## Update Data Agent

Fetch the website content and update data files.

**Instructions:**

- You should identify the website url from the input month. I have listed the urls for each month in `README.md` file.
- Fetch the content from the website.
- Parse the data from the website content.
- Update the corresponding data files (`monthly-cases.csv` and `monthly-deaths.csv` for monthly data and `yearly-cases.csv` and `yearly-deaths.csv` for yearly data) in the `data/` folder. Do not use Python; instead, update the files directly.
- If you find some columns are missing in the data files, stop and inform me about the missing columns.
- Avoid running any code or scripts. Only update the data files directly.
- After updating the data files, run the unit tests using the `runTests` tool (with `check.py` as the test file) to verify the changes.
- Tell me the changes you made to the data files and the test results.

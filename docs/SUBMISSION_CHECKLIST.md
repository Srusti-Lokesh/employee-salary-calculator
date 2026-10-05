# Submission Checklist

## Before GitHub push

- [ ] Run `pytest -q` and confirm all tests pass.
- [ ] Run `python app.py` and verify the calculator in a browser.
- [ ] Test a valid employee.
- [ ] Test invalid/empty salary input.
- [ ] Open `/health` and confirm `{"status":"ok"}`.
- [ ] Confirm no `.venv`, passwords, API keys, or local secrets are committed.

## GitHub evidence

Capture screenshots showing:

1. Public repository home page.
2. README with project description and setup instructions.
3. Source files/tests in the repository.
4. Commit history showing your project work.

## Render evidence

Capture screenshots showing:

1. Render service settings (build command/start command/branch).
2. Successful deployment status.
3. Live application URL in the browser.
4. `/health` returning `{"status":"ok"}`.
5. At least one salary calculation result.
6. Deploy history showing a successful earlier deployment. If required by the internship, demonstrate a rollback to that known-good deploy and capture the result.

## Submission package

Submit:

- GitHub repository URL.
- Live Render URL.
- Project ZIP if the portal requests a ZIP.
- Project report PDF.
- Screenshots/evidence requested by the internship portal.

## Suggested final links section

```text
GitHub: https://github.com/YOUR-USERNAME/employee-salary-calculator
Live Demo: https://YOUR-RENDER-SERVICE.onrender.com
Report: Employee_Salary_Calculator_Project_Report.pdf
```

# Employee Salary Calculator

A Python + Flask web application that calculates employee gross salary, configurable allowances, deductions, progressive income tax, and net salary.

> **Educational project:** the included percentages and tax brackets are sample rules created for this assignment. They are not legal, statutory, or payroll advice.

## Features

- Employee input validation.
- Dictionary-based employee records and configurable salary rules.
- Separate functions for allowances, progressive tax, deductions, and final salary.
- Salary calculation breakdown for transparency.
- Responsive Flask web interface.
- `/health` endpoint for deployment health checks.
- Sample employee records in `data/sample_employees.json`.
- Automated tests with pytest.
- Render deployment configuration in `render.yaml`.

## Project structure

```text
employee_salary_calculator/
├── app.py
├── salary_calculator.py
├── salary_rules.py
├── requirements.txt
├── render.yaml
├── README.md
├── .gitignore
├── data/
│   └── sample_employees.json
├── docs/
│   └── SUBMISSION_CHECKLIST.md
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── result.html
└── tests/
    ├── test_app.py
    └── test_salary_calculator.py
```

## Local setup on Windows PowerShell

From the project folder:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
python app.py
```

Open `http://127.0.0.1:5000` in a browser. Keep the PowerShell window running while testing.

If PowerShell blocks activation, run this once in the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## GitHub

Create an empty public GitHub repository named `employee-salary-calculator` (do not initialize it with another README/license/gitignore). Then from this project folder:

```powershell
git init
git branch -M main
git add .
git commit -m "Build employee salary calculator"
git remote add origin https://github.com/YOUR-USERNAME/employee-salary-calculator.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Render deployment

This repository includes `render.yaml`, so the deployment settings are already defined.

Recommended Dashboard settings if entering them manually:

- Service: **Web Service**
- Repository: this GitHub repository
- Branch: `main`
- Runtime: **Python 3**
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Health check path: `/health`
- Plan: Free (if available to your account)
- Auto-deploy: On

After deployment, Render provides a public `onrender.com` URL. Test both `/` and `/health`.

## Salary calculation logic

1. Base salary is read from the employee record.
2. Each configured allowance is calculated as a percentage of base salary.
3. Gross salary = base salary + total allowances.
4. Percentage deductions are calculated from gross salary.
5. Progressive income tax is calculated using the ordered brackets in `salary_rules.py`.
6. Total deductions = percentage deductions + income tax.
7. Net salary = gross salary - total deductions.

## Changing business rules

Edit only `salary_rules.py` for the normal assignment scenario. For example, changing `housing` from `0.20` to `0.25` changes the allowance without rewriting the calculation functions.

## Rollback evidence

For the assignment's rollback requirement, deploy a working commit first. If a later deployment has a problem, use Render's **Deploys** page to select the previous successful deploy and click **Rollback**. Record the old/new commit IDs and take a screenshot of the rollback/deploy history for submission.

## Interview questions

**How would you represent employee data?**  
Use dictionaries for individual employee records and a list of dictionaries for multiple employees. This keeps the data readable and easy to validate or serialize as JSON.

**Why should business rules be separated from input handling?**  
It keeps the UI/request layer focused on validation and presentation while the calculation layer remains reusable, testable, and independent of Flask.

**How would you modify the program if salary rules changed?**  
Update the configuration in `salary_rules.py` rather than rewriting the calculation flow. Tests can then be updated to verify the new rules.

## License

For internship/educational submission use.

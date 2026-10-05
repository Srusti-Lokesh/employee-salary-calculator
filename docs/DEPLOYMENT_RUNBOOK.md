# Deployment Runbook — Windows PowerShell → GitHub → Render

This runbook is written for the project exactly as provided. Follow the steps in order.

## 1. Install/check prerequisites

Open **PowerShell** and run:

```powershell
py --version
git --version
```

You need Python and Git installed. If `py` is not recognized, install Python from the official Python website and reopen PowerShell. If `git` is not recognized, install Git and reopen PowerShell.

## 2. Open the project folder

If you extracted the ZIP into Downloads, for example:

```powershell
cd "$HOME\Downloads\employee_salary_calculator"
```

If your folder is somewhere else, change the path accordingly. Confirm the important files exist:

```powershell
Get-ChildItem
```

You should see `app.py`, `salary_calculator.py`, `salary_rules.py`, `requirements.txt`, `render.yaml`, `README.md`, `templates`, `static`, `tests`, and `data`.

## 3. Create and activate the virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The prompt should show `(.venv)`.

## 4. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Run tests

```powershell
pytest -q
```

Expected result: all tests pass. Do not push to GitHub if tests are failing.

## 6. Run the application locally

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Test:

- valid employee ID/name/department/base salary;
- empty fields;
- non-numeric salary;
- zero/negative salary;
- the salary result and breakdown;
- `http://127.0.0.1:5000/health`.

Expected health response:

```json
{"status":"ok"}
```

Stop the server with `Ctrl+C`.

## 7. Create the GitHub repository

On GitHub, choose **New repository**.

Recommended values:

- Repository name: `employee-salary-calculator`
- Description: `A Python Flask employee salary calculator with configurable allowances, deductions, progressive tax rules, validation, tests, and Render deployment configuration.`
- Visibility: **Public** (the assignment explicitly asks for a public GitHub repository).
- Do **not** initialize the repository with another README, `.gitignore`, or license because this project already contains those files.

## 8. Push from PowerShell

From the project folder:

```powershell
git init
git branch -M main
git add .
git status
git commit -m "Build employee salary calculator"
git remote add origin https://github.com/YOUR-USERNAME/employee-salary-calculator.git
git remote -v
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

If Git asks for authentication, complete GitHub's browser/credential flow. Never put a password or personal access token into a source file.

## 9. Verify GitHub

Refresh the repository page. Confirm these are visible:

- README.md
- app.py
- salary_calculator.py
- salary_rules.py
- render.yaml
- requirements.txt
- tests/
- templates/
- static/
- data/

Do **not** upload `.venv`.

## 10. Deploy on Render

1. Sign in to Render.
2. Select **New → Web Service**.
3. Connect your GitHub account if requested.
4. Select `employee-salary-calculator`.
5. Branch: `main`.
6. Runtime/language: Python.
7. Build command: `pip install -r requirements.txt`.
8. Start command: `gunicorn app:app`.
9. Health check path: `/health`.
10. Choose the Free plan if it is available for the assignment/account.
11. Enable automatic deploys from `main`.
12. Create the web service.

The included `render.yaml` contains these settings as deployment configuration as well.

## 11. Verify the live deployment

Render will give you a URL similar to:

```text
https://employee-salary-calculator.onrender.com
```

Your exact hostname may differ.

Open:

```text
https://YOUR-RENDER-SERVICE.onrender.com/
https://YOUR-RENDER-SERVICE.onrender.com/health
```

Then calculate a sample employee. Save screenshots of:

1. Render deployment succeeded.
2. Live application page.
3. Salary calculation result.
4. Health endpoint.

## 12. Create rollback evidence

The assignment asks for rollback evidence. Do not fake this screenshot.

After the first successful deployment:

```powershell
git log --oneline --decorate -5
```

Record the successful commit SHA.

Then make a harmless visible change, commit it, and push:

```powershell
git add .
git commit -m "Update project documentation"
git push
```

Wait for the second deployment to succeed. In Render, open **Deploys** and note both successful deploys.

If your assignment specifically requires demonstrating rollback, select the earlier known-good deployment and use **Rollback**. Render's rollback feature reuses the earlier successful deploy artifact. After rollback completes, open the live URL and verify the application again.

Take a screenshot showing the deploy history/rollback result and keep the commit IDs in your submission notes.

## 13. Final GitHub update

If you added any evidence notes or documentation:

```powershell
git status
git add .
git commit -m "Document deployment and rollback evidence"
git push
```

Do not commit private Render credentials, tokens, or secrets.

## 14. Final submission checklist

Submit the following in the internship portal:

- Public GitHub repository URL.
- Live Render URL.
- Project ZIP file, if requested.
- Project report PDF.
- Screenshots/evidence requested by the portal.
- Rollback evidence screenshot if required.

Recommended final link format:

```text
GitHub: https://github.com/YOUR-USERNAME/employee-salary-calculator
Live Demo: https://YOUR-RENDER-SERVICE.onrender.com
```

from flask import Flask, render_template, request
from salary_calculator import calculate_salary, validate_employee
from salary_rules import SALARY_RULES

app = Flask(__name__)
app.config["SECRET_KEY"] = "employee-salary-calculator-dev"


@app.get("/")
def index():
    return render_template("index.html", rules=SALARY_RULES)


@app.post("/calculate")
def calculate():
    employee = {
        "employee_id": request.form.get("employee_id", "").strip(),
        "name": request.form.get("name", "").strip(),
        "department": request.form.get("department", "").strip(),
        "base_salary": request.form.get("base_salary", "").strip(),
    }

    errors = validate_employee(employee)
    if errors:
        return render_template("index.html", rules=SALARY_RULES, employee=employee, errors=errors), 400

    result = calculate_salary(employee, SALARY_RULES)
    return render_template("result.html", employee=result["employee"], breakdown=result, rules=SALARY_RULES)


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

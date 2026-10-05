"""Configurable salary rules for the Employee Salary Calculator.

These are sample educational rules only. Change the values here to model a
course/project scenario; they are not intended to represent legal payroll rules.
"""

SALARY_RULES = {
    "allowances": {
        "housing": {"label": "Housing Allowance", "rate": 0.20},
        "transport": {"label": "Transport Allowance", "rate": 0.10},
        "bonus": {"label": "Performance Bonus", "rate": 0.05},
    },
    "deductions": {
        "provident_fund": {"label": "Provident Fund", "rate": 0.12},
        "insurance": {"label": "Insurance", "rate": 0.02},
    },
    "tax_brackets": [
        {"up_to": 50000, "rate": 0.10},
        {"up_to": 100000, "rate": 0.15},
        {"up_to": None, "rate": 0.20},
    ],
}

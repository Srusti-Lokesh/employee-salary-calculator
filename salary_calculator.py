"""Business logic for employee salary calculations."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

TWOPLACES = Decimal("0.01")


def money(value):
    """Convert a number-like value to Decimal rounded to two decimals."""
    return Decimal(str(value)).quantize(TWOPLACES, rounding=ROUND_HALF_UP)


def validate_employee(employee):
    """Return a list of validation errors for an employee dictionary."""
    errors = []
    if not employee.get("employee_id"):
        errors.append("Employee ID is required.")
    if not employee.get("name"):
        errors.append("Employee name is required.")
    if not employee.get("department"):
        errors.append("Department is required.")

    raw_salary = employee.get("base_salary", "")
    try:
        salary = Decimal(str(raw_salary))
        if salary <= 0:
            errors.append("Base salary must be greater than 0.")
    except (InvalidOperation, ValueError):
        errors.append("Base salary must be a valid number.")
    return errors


def calculate_allowances(base_salary, rules):
    """Calculate all configured allowances from base salary."""
    return {
        key: money(base_salary * Decimal(str(item["rate"])))
        for key, item in rules["allowances"].items()
    }


def calculate_progressive_tax(taxable_income, brackets):
    """Calculate progressive tax using ordered tax brackets."""
    taxable_income = money(taxable_income)
    tax = Decimal("0")
    previous_limit = Decimal("0")

    for bracket in brackets:
        upper = bracket["up_to"]
        rate = Decimal(str(bracket["rate"]))
        if upper is None:
            amount_in_band = max(taxable_income - previous_limit, Decimal("0"))
        else:
            upper_decimal = Decimal(str(upper))
            amount_in_band = max(min(taxable_income, upper_decimal) - previous_limit, Decimal("0"))
        tax += amount_in_band * rate
        if upper is None or taxable_income <= Decimal(str(upper)):
            break
        previous_limit = Decimal(str(upper))

    return money(tax)


def calculate_deductions(gross_salary, rules):
    """Calculate configured percentage deductions plus progressive tax."""
    percentage_deductions = {
        key: money(gross_salary * Decimal(str(item["rate"])))
        for key, item in rules["deductions"].items()
    }
    percentage_total = sum(percentage_deductions.values(), Decimal("0"))
    tax = calculate_progressive_tax(gross_salary, rules["tax_brackets"])
    return percentage_deductions, tax, money(percentage_total + tax)


def calculate_salary(employee, rules):
    """Return a complete salary breakdown for an employee."""
    base = money(employee["base_salary"])
    allowances = calculate_allowances(base, rules)
    total_allowances = money(sum(allowances.values(), Decimal("0")))
    gross = money(base + total_allowances)

    deductions, tax, total_deductions = calculate_deductions(gross, rules)
    deductions = {**deductions, "income_tax": tax}
    net = money(gross - total_deductions)

    return {
        "employee": {
            **employee,
            "base_salary": base,
        },
        "base_salary": base,
        "allowances": allowances,
        "total_allowances": total_allowances,
        "gross_salary": gross,
        "deductions": deductions,
        "total_deductions": total_deductions,
        "net_salary": net,
    }

from decimal import Decimal
from salary_calculator import calculate_progressive_tax, calculate_salary, validate_employee
from salary_rules import SALARY_RULES


def test_validation_rejects_invalid_salary():
    errors = validate_employee({"employee_id": "E1", "name": "Test", "department": "IT", "base_salary": "abc"})
    assert "Base salary must be a valid number." in errors


def test_progressive_tax_brackets():
    assert calculate_progressive_tax(Decimal("40000"), SALARY_RULES["tax_brackets"]) == Decimal("4000.00")
    assert calculate_progressive_tax(Decimal("60000"), SALARY_RULES["tax_brackets"]) == Decimal("6500.00")
    assert calculate_progressive_tax(Decimal("120000"), SALARY_RULES["tax_brackets"]) == Decimal("16500.00")


def test_salary_breakdown():
    employee = {"employee_id": "E1", "name": "Test User", "department": "IT", "base_salary": "60000"}
    result = calculate_salary(employee, SALARY_RULES)
    assert result["total_allowances"] == Decimal("21000.00")
    assert result["gross_salary"] == Decimal("81000.00")
    assert result["total_deductions"] == Decimal("20990.00")
    assert result["net_salary"] == Decimal("60010.00")

from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_calculate_page():
    client = app.test_client()
    response = client.post("/calculate", data={
        "employee_id": "EMP001",
        "name": "Aarav Sharma",
        "department": "Engineering",
        "base_salary": "60000",
    })
    assert response.status_code == 200
    assert b"Salary Breakdown" in response.data
    assert b"60010.00" in response.data

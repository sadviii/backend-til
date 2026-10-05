from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_employee():
    login_response = client.post("/login")

    token = login_response.json()["access_token"]

    response = client.get(
        "/employees/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

 def test_employee_not_found():
    login_response = client.post("/login")

    token = login_response.json()["access_token"]

    response = client.get(
        "/employees/99999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Employee not found"

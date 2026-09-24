import jwt
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Header
from pydantic import BaseModel

from database import SessionLocal, Employee


app = FastAPI()

secret_key = "my-super-secret-key-for-jwt-demo-12345"


class EmployeeCreate(BaseModel):
    name: str
    department: str


permissions = {
    "employee": ["read"],
    "manager": ["read", "update"],
    "admin": ["read", "update", "create", "delete"]
}


@app.post("/login")
def login():
    payload = {
        "user_id": 5,
        "role": "employee",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        secret_key,
        algorithm="HS256"
    )

    return {"access_token": token}


@app.get("/employees")
def get_employees(authorization: str = Header(...)):
    parts = authorization.split(" ")

    if len(parts) != 2 or parts[0] != "Bearer":
        return {"message": "Invalid authorization header"}

    token = parts[1]

    try:
        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}

    role = decoded["role"]

    if role not in permissions or "read" not in permissions[role]:
        return {"message": "Read not allowed"}

    session = SessionLocal()

    employees = session.query(Employee).all()

    session.close()

    return employees


@app.get("/employees/{employee_id}")
def get_employee(
    employee_id: int,
    authorization: str = Header(...)
):
    parts = authorization.split(" ")

    if len(parts) != 2 or parts[0] != "Bearer":
        return {"message": "Invalid authorization header"}

    token = parts[1]

    try:
        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}

    role = decoded["role"]

    if role not in permissions or "read" not in permissions[role]:
        return {"message": "Read not allowed"}

    session = SessionLocal()

    employee = session.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    session.close()

    if employee:
        return employee

    return {"message": "Employee not found"}


@app.post("/employees")
def create_employee(
    employee_data: EmployeeCreate,
    authorization: str = Header(...)
):
    parts = authorization.split(" ")

    if len(parts) != 2 or parts[0] != "Bearer":
        return {"message": "Invalid authorization header"}

    token = parts[1]

    try:
        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}

    role = decoded["role"]

    if role not in permissions or "create" not in permissions[role]:
        return {"message": "Create not allowed"}

    session = SessionLocal()

    employee = Employee(
        name=employee_data.name,
        department=employee_data.department
    )

    session.add(employee)
    session.commit()
    session.refresh(employee)

    session.close()

    return employee


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee_data: EmployeeCreate,
    authorization: str = Header(...)
):
    parts = authorization.split(" ")

    if len(parts) != 2 or parts[0] != "Bearer":
        return {"message": "Invalid authorization header"}

    token = parts[1]

    try:
        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}

    role = decoded["role"]

    if role not in permissions or "update" not in permissions[role]:
        return {"message": "Update not allowed"}

    session = SessionLocal()

    employee = session.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        session.close()
        return {"message": "Employee not found"}

    employee.name = employee_data.name
    employee.department = employee_data.department

    session.commit()
    session.refresh(employee)

    session.close()

    return employee


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    authorization: str = Header(...)
):
    parts = authorization.split(" ")

    if len(parts) != 2 or parts[0] != "Bearer":
        return {"message": "Invalid authorization header"}

    token = parts[1]

    try:
        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}

    role = decoded["role"]

    if role not in permissions or "delete" not in permissions[role]:
        return {"message": "Delete not allowed"}

    session = SessionLocal()

    employee = session.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        session.close()
        return {"message": "Employee not found"}

    session.delete(employee)
    session.commit()

    session.close()

    return {"message": "Employee deleted"}
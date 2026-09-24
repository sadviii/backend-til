```markdown
# End-to-End Employee API

## Overview

Built a complete Employee Management backend using FastAPI, SQLAlchemy ORM, SQLite, JWT Authentication, and Role-Based Authorization.

The project combines HTTP requests, RESTful API design, database operations, authentication, and authorization into one working backend.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- PyJWT

## Topics Covered

- HTTP Methods: GET, POST, PUT, DELETE
- RESTful API Design
- FastAPI
- Path Parameters
- Request Headers
- Request Body Validation
- SQLite Database
- SQLAlchemy ORM
- Database Sessions
- CRUD Operations
- JWT Authentication
- JWT Signature Verification
- JWT Expiration
- Bearer Token Authentication
- Role-Based Access Control (RBAC)
- Roles and Permissions
- Protected API Endpoints

## Project Structure

```text
employee-api/
├── main.py
├── database.py
├── seed.py
├── employee.db
└── README.md
```

## API Endpoints

| Method | Endpoint | Purpose | Permission |
|---|---|---|---|
| POST | `/login` | Generate JWT | Public |
| GET | `/employees` | Get all employees | `read` |
| GET | `/employees/{employee_id}` | Get one employee | `read` |
| POST | `/employees` | Create employee | `create` |
| PUT | `/employees/{employee_id}` | Update employee | `update` |
| DELETE | `/employees/{employee_id}` | Delete employee | `delete` |

## Roles and Permissions

```python
permissions = {
    "employee": ["read"],
    "manager": ["read", "update"],
    "admin": ["read", "update", "create", "delete"]
}
```

### Authorization Rules

```text
employee → read
manager  → read, update
admin    → read, update, create, delete
```

## Authentication Flow

The `/login` endpoint creates a JWT containing:

- `user_id`
- `role`
- `exp`

The client sends the token using:

```text
Authorization: Bearer <JWT>
```

The backend then:

1. Extracts the Bearer token.
2. Verifies the JWT signature.
3. Reads the verified role.
4. Checks the role's permissions.
5. Allows or rejects the requested action.

## Database Flow

```text
HTTP Request
     ↓
FastAPI
     ↓
JWT Authentication
     ↓
Authorization
     ↓
SQLAlchemy ORM
     ↓
SQLite Database
     ↓
HTTP Response
```

## Hands-on Practice

Implemented and tested:

- GET all employees
- GET a single employee
- Create an employee
- Update an employee
- Delete an employee
- JWT generation
- JWT verification
- Expired token handling
- Invalid token handling
- Bearer token extraction
- Role-based authorization
- Permission checks
- Database persistence

## Authorization Testing

Verified the following behavior:

```text
Employee
→ Read ✅
→ Create ❌
→ Update ❌
→ Delete ❌

Manager
→ Read ✅
→ Create ❌
→ Update ✅
→ Delete ❌

Admin
→ Read ✅
→ Create ✅
→ Update ✅
→ Delete ✅
```

Also tested invalid JWTs and unauthorized actions.

## Key Takeaways

- Authentication answers **"Who are you?"**
- Authorization answers **"What are you allowed to do?"**
- JWTs contain claims such as user ID, role, and expiration.
- JWT payloads are encoded, not encrypted.
- JWT signatures help detect unauthorized token modification.
- The backend should use the verified JWT payload for authorization.
- RBAC maps roles to permissions.
- Unknown or unauthorized roles should be denied.
- SQLAlchemy ORM allows Python objects to interact with database tables.
- `session.commit()` persists database changes.
- FastAPI automatically generates interactive API documentation through Swagger UI.

## Final Competency

Successfully built an end-to-end Employee Management API that:

- Exposes RESTful CRUD endpoints.
- Stores employee data in SQLite.
- Uses SQLAlchemy ORM for database operations.
- Generates and verifies JWTs.
- Uses Bearer token authentication.
- Implements role-based authorization.
- Restricts create, update, and delete operations based on permissions.
- Handles invalid tokens and unauthorized actions.
- Persists and retrieves data from the database.


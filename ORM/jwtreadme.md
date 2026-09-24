# JWT Authentication & Authorization

## Topics Covered

* Authentication vs Authorization
* JSON Web Tokens (JWT)
* JWT structure:

  * Header
  * Payload
  * Signature
* JWT claims and expiration
* Creating JWTs using PyJWT
* Decoding and verifying JWTs
* JWT signature verification
* Handling expired tokens
* Handling invalid tokens
* Role-Based Access Control (RBAC)
* Roles and permissions
* Authorization checks
* Deny-by-default behavior
* Using verified JWT payloads for authorization

## Hands-on Practice

Built a JWT authentication and authorization flow using Python and PyJWT.

### JWT Creation

Created a JWT containing user information and role:

```python
payload = {
    "user_id": 5,
    "role": "employee"
}

token = jwt.encode(
    payload,
    secret_key,
    algorithm="HS256"
)
```

### JWT Verification

Verified the JWT using the secret key:

```python
decoded = jwt.decode(
    token,
    secret_key,
    algorithms=["HS256"]
)
```

The decoded payload was used only after successful signature verification.

### Authorization / RBAC

Defined permissions based on roles:

```python
permissions = {
    "employee": ["read"],
    "manager": ["read", "update"],
    "admin": ["read", "update", "delete"]
}
```

Checked whether a user's verified role had permission to perform an action:

```python
if role in permissions and action in permissions[role]:
    print("action allowed")
else:
    print("action denied")
```

### Security Testing

Tested:

* Valid JWT with the correct secret
* Expired JWT
* Invalid JWT signature
* Wrong verification secret
* Unknown roles
* Different roles with different permissions

An invalid JWT was rejected without allowing authorization to proceed.

## Key Takeaways

* Authentication answers **"Who are you?"**
* Authorization answers **"What are you allowed to do?"**
* JWTs can carry claims such as user ID, role, and expiration.
* JWT payloads are encoded, not encrypted.
* The signature helps detect unauthorized modification.
* Authoriz

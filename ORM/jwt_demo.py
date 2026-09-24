#import jwt
#import time
#from datetime import datetime, timedelta, timezone

secret_key = "my-super-secret-key-for-jwt-demo-12345"

"""payload = {
    "user_id": 1,
    "role": "employee",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}


token = jwt.encode(
    payload,
    secret_key,
    algorithm="HS256"
)

print(token)

time.sleep(3)

try:
    decoded = jwt.decode(
        token,
        "wrong-secret-key",
        algorithms=["HS256"]
    )

    print(decoded)

except jwt.ExpiredSignatureError:
    print("Token has expired")"""

import jwt
import time
from datetime import datetime, timedelta, timezone

secret_key = "my-super-secret-key-for-jwt-demo-12345"
payload = {
    "user_id": 5,
    "role": "employee"
}

token = jwt.encode(
    payload,
    "wrong-secret-key",
    algorithm="HS256"
)
try:
    decoded = jwt.decode(
        token,
        secret_key,
        algorithms=["HS256"]
        
    )
    role = decoded["role"]
    permissions = {
    "employee": ["read"],
    "manager": ["read", "update"],
    "admin": ["read", "update", "delete"]
}

    print(decoded)

    action = "update"

    if role in permissions and action in permissions[role]:
        print("action allowed")
    else:
        print("action denied")


except jwt.InvalidTokenError:
    print("Invalid token") 







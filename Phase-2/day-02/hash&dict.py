"""You're building a backend system that tracks currently active users.

Create:

sessions = {}

Your program must:

Add 5 users with unique user IDs.
Store each user's name and status.
Update one user's status from "offline" to "online".
Check whether a specific user ID exists.
Safely retrieve another user's session using .get().
Remove one user's session.
Print the remaining sessions.
Print the total number of active sessions.
Your constraints
Use a dictionary as the main data structure.
Choose the nested structure yourself.
Don't copy the previous inventory example exactly.
You should be able to explain why a dictionary is appropriate here, especially in terms of lookup complexity."""


sessions = {
    "U101": {"name": "Alice", "status": "online"},
    "U102": {"name": "Bob", "status": "offline"},
    "U103": {"name": "Charlie", "status": "online"},
    "U104": {"name": "David", "status": "offline"},
    "U105": {"name": "Eve", "status": "online"}
}
sessions["U102"]["status"] = "online"
print("U101" in sessions)
print(sessions.get("U103"))
del sessions["U101"]
print(sessions)
active_sessions = 0

for session in sessions.values():
    if session["status"] == "online":
        active_sessions += 1

print(f"Total active sessions: {active_sessions}")
#print(f"Total active sessions: {len(sessions)}")

















"""user = {
    "id": "U101",
    "name": "Alice",
    "role": "user"
}
 
user["role"] = "admin"
user['email'] = "alice@example.com"
print("email" in user)
print(user)"""

"""users = {
    "U101": {"name": "Alice", "role": "admin"},
    "U102": {"name": "Bob", "role": "user"},
    "U103": {"name": "Charlie", "role": "user"},
    "U104": {"name": "David", "role": "user"}
}
users["U102"]["role"] = "admin"
del users["U103"]
print("U104" in users)
print(users)"""




"""Build a small user session manager using a dictionary.

Start with:

sessions = {}

Your program should:

Add these sessions:
U101 → "Alice"
U102 → "Bob"
U103 → "Charlie"
Update U102's user name to "Robert".
Check whether U101 exists.
Retrieve U103 safely using .get().
Delete U101.
Print the final dictionary.

Important: Decide the dictionary structure yourself. Don't worry about making it fancy."""


"""sessions = {
    "U101": "Alice",
    "U102": "Bob",
    "U103": "Charlie"
}
sessions["U102"] = "Robert"
print("U101" in sessions)
print(sessions.get("U103"))
del sessions["U101"]
print(sessions)"""


"""Build a product inventory using a dictionary.

Requirements

Your program should:

Start with an empty dictionary.
Add at least 4 products, each with:
Product ID
Product name
Stock quantity
Update the stock quantity of one product.
Check whether a particular product ID exists.
Safely retrieve a product using .get().
Delete one product.
Print the final inventory."""

"""inventory = {
    "P001": {"name": "Laptop", "stock": 10},
    "P002": {"name": "Smartphone", "stock": 25},
    "P003": {"name": "Headphones", "stock": 50},
    "P004": {"name": "Monitor", "stock": 15} }

inventory["P002"]["stock"] = 30
print("P001" in inventory)
print(inventory.get("P003"))
del inventory["P001"]
print(inventory)"""
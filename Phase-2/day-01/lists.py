"""You are building a backend system that tracks online users:

online_users = ["U101", "U102", "U103", "U104"]

The following events happen in this exact order:

U105 comes online → add it to the list.
U102 goes offline → remove it.
An admin user ADMIN01 comes online → place it at the beginning.
U103 completes verification → change it to U103_verified.
The backend needs to check whether U104 is currently online.
Print whether U104 is online.
Print the final list.
Print the total number of online users"""


online_users = ["U101", "U102", "U103", "U104"]

online_users.append("U105")
online_users.remove("U102")
online_users.insert(0, "ADMIN01")
online_users[online_users.index("U103")] = "U103_verified"

is_u104_online = "U104" in online_users
print(f"Is U104 online? {is_u104_online}")

print("Final list of online users:")
print(online_users)

print(f"Total number of online users: {len(online_users)}")

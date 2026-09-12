# Day 2 — Hash Maps / Dictionaries

## Topics Covered

### 1. Understanding Dictionaries

Learned that dictionaries store data as key-value pairs, where each key uniquely identifies a value.

### 2. Dictionary Operations

Learned how to:

* Create dictionaries
* Access values using `[]`
* Add and update key-value pairs
* Delete entries using `del` and `pop()`
* Check key existence using `in`
* Safely retrieve values using `.get()`

### 3. Iterating Through Dictionaries

Learned how to use:

* `.keys()`
* `.values()`
* `.items()`
* Direct iteration through keys

### 4. Hashing

Learned how dictionary keys are processed through a hash function to efficiently locate stored data.

### 5. Hash Collisions

Learned that different keys can map to the same hash-table location and that dictionaries handle these collisions internally.

### 6. Dictionary Performance

Learned that dictionary lookup, insertion, and deletion are **O(1) average**.

### 7. Hashable Keys

Learned that dictionary keys must be hashable and that mutable types such as lists cannot be used as keys.

### 8. Nested Dictionaries

Learned how dictionaries can contain other dictionaries to represent structured data.

### 9. Dictionary Memory and Resizing

Learned that dictionaries resize their internal hash table as they grow. Individual resizing operations can be expensive, but insertion remains **O(1) amortized**.

### 10. Backend Applications

Learned how dictionaries can be used for:

* User sessions
* User ID lookups
* Product inventories
* Structured backend records

## Hands-on Practice

* Created and modified user dictionaries.
* Built a nested user-session dictionary.
* Built a product inventory using nested dictionaries.
* Completed an independent dictionary exercise.
* Completed the User Session Manager competency task.

## Key Takeaways

* Dictionaries store **key-value pairs**.
* Keys provide efficient direct lookup.
* Dictionary lookup is **O(1) average**.
* Dictionaries handle hashing, collisions, and resizing internally.
* Nested dictionaries are useful for structured backend data.
* Dictionary insertion is **O(1) amortized** because resizing can occasionally require additional work.

## Final Practice / Competency

Built a user session manager that:

* Stores users by unique ID.
* Tracks name and status.
* Updates session status.
* Checks user existence.
* Safely retrieves sessions with `.get()`.
* Deletes sessions.
* Counts only sessions whose status is `"online"`.



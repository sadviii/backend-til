# Day 1 — Arrays / Lists

## Topics Covered

### 1. Understanding Lists

Learned that Lists are ordered collections used to store multiple values together.

Understood why Lists are useful for maintaining collections of data and preserving the order of elements.

### 2. Contiguous Memory

Learned the concept of contiguous memory and how array-based structures store elements in neighboring memory locations.

Understood that Python `list` is implemented as a dynamic array that stores references to Python objects.

### 3. Indexing

Learned that Python Lists use zero-based indexing.

Practiced accessing elements using positive and negative indexes.

```python
products[0]
products[2]
products[-1]
```

### 4. Iteration

Learned how to iterate through Lists using `for` loops.

Practiced both direct value-based iteration and index-based iteration.

```python
for user in users:
    print(user)
```

```python
for i in range(len(scores)):
    print(scores[i])
```

### 5. Insertion

Learned how to add elements to Lists using:

* `append()` → Adds an element to the end.
* `insert()` → Adds an element at a specific index.

Understood that inserting into the middle can shift subsequent elements.

### 6. Deletion

Learned different ways to remove elements:

* `remove()` → Removes an element by value.
* `pop()` → Removes an element by index and returns it.
* `del` → Deletes an element or slice.

Understood that deleting elements can cause indexes of later elements to change.

### 7. Searching

Learned how to search Lists using:

* `in` → Checks whether a value exists.
* `index()` → Finds the index of a value.

Understood that `index()` raises a `ValueError` when the value is not found.

### 8. Updating Elements

Learned that Python Lists are mutable and existing elements can be changed using their index.

```python
scores[1] = 80
```

Understood the difference between updating, inserting, and deleting an element.

### 9. Python List Behavior

Learned that Python Lists:

* Are mutable
* Allow duplicate values
* Can contain different data types
* Support negative indexing
* Support slicing
* Have dynamic size

Practiced common List operations including:

```python
append()
insert()
remove()
pop()
index()
count()
sort()
reverse()
len()
```

### 10. When to Use and Avoid Lists

Learned that Lists are a good choice when:

* Data needs to remain ordered.
* Fast access by position is required.
* Data needs to be iterated through.

Learned that Lists are not ideal when the main requirement is frequent lookup by an identifier or value, especially as the dataset becomes large.

### 11. Practical Exercises

Practiced List operations through progressively harder exercises involving:

* Student records
* Product searching and updating
* Orders
* Shopping carts
* Backend-style API requests
* Online user tracking

Practiced combining multiple List operations and choosing the appropriate operation based on the requirement.

### 12. Lists Competency Task

Completed a backend-style online user management task from scratch.

The task involved:

* Adding a user
* Removing a user
* Inserting an admin at the beginning
* Updating a user using its index
* Searching for a user
* Printing the final List
* Calculating the number of users

Successfully completed the task independently.

### Key Takeaways

* Lists maintain order.
* Python Lists use zero-based indexing.
* Python `list` is a dynamic array.
* Lists are mutable.
* Indexes can change after insertion or deletion.
* Lists provide fast positional access.
* Searching through a List becomes less efficient as the collection grows.
* Choosing a data structure depends on how the data will be accessed and modified.



# Day 3 — Memory Management

## Topics Covered

### 1. Variables, Objects and References
Learned that variables in Python are names that refer to objects rather than directly storing the objects themselves.
Multiple variables can refer to the same object.

### 2. Mutable vs Immutable Objects
Learned that immutable objects cannot be changed after creation, while mutable objects can be modified.
Examples include integers and strings as immutable, and lists and dictionaries as mutable.

### 3. Pass-by-Value vs Pass-by-Reference
Learned that Python passes object references to functions, commonly described as pass-by-object-reference.
Reassigning a parameter does not affect the original variable, while mutating a mutable object can affect the original object.

### 4. Unintended Variable Mutations
Learned how modifying mutable objects inside functions can unintentionally change the original data.
Understanding references and mutation helps prevent unexpected changes.

### 5. Shallow Copy
Learned that a shallow copy creates a new outer object while nested objects may still be shared.
Practiced using `.copy()` with lists.

### 6. Deep Copy
Learned that deep copying creates independent copies of nested objects as well.
Practiced using `copy.deepcopy()` to prevent changes to nested data from affecting the original.

### 7. Garbage Collection
Learned that Python automatically manages objects that are no longer reachable.
Garbage collection helps reclaim memory occupied by objects that are no longer needed.

### 8. References and Object Lifetime
Learned that an object remains reachable as long as references to it exist.
When an object becomes unreachable, Python can reclaim its memory.

### 9. Memory Leaks
Learned that unnecessary references can keep objects in memory even when the program no longer needs them.
Avoiding unnecessary long-lived references helps reduce memory problems.

## Hands-on Practice

- Practiced variables, objects, and references
- Used `id()` to understand object identity
- Practiced mutable and immutable objects
- Practiced passing lists to functions
- Demonstrated unintended mutations
- Used shallow copies with `.copy()`
- Used deep copies with `copy.deepcopy()`
- Practiced understanding references and `del`
- Learned the basics of garbage collection
- Practiced identifying potential memory problems
- Built a memory-management example from a blank file

## Key Takeaways

- Variables/names refer to objects.
- Multiple variables can refer to the same object.
- Mutable objects can be changed after creation.
- Immutable objects cannot be changed after creation.
- Python passes object references to functions.
- Reassignment and mutation are different.
- Shallow copy → new outer object, nested objects may be shared.
- Deep copy → independent nested objects.
- Unreachable objects can be reclaimed by garbage collection.
- Unnecessary references can cause memory problems.


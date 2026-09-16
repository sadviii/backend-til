Here’s the concise TIL-style README for **Big-O / Time & Space Complexity**, matching the format we used for the previous topics.

# Big-O — Time & Space Complexity

## Topics Covered

### 1. Big-O Notation

* Describes how an algorithm's time or memory usage grows as input size `N` increases.
* Focuses on growth rate rather than exact runtime.

### 2. Common Time Complexities

* **O(1)** — constant time
* **O(N)** — linear time
* **O(N²)** — quadratic time
* **O(N × M)** — when two different input sizes are involved

### 3. Sequential vs Nested Loops

* Sequential loops → add their complexity.

  * `O(N) + O(N)` → `O(N)`
* Nested loops → multiply their complexity.

  * `O(N) × O(N)` → `O(N²)`
  * Different inputs → `O(N × M)`

### 4. Best & Worst Case

* Best case → minimum amount of work.
* Worst case → maximum amount of work.
* Example: searching a list:

  * Best → `O(1)` if the target is first.
  * Worst → `O(N)` if the target is last or absent.

### 5. Time vs Space Complexity

* **Time complexity** → how much work the algorithm performs.
* **Space complexity** → additional memory that grows with the input.

Examples:

* One variable → `O(1)` space.
* Growing list/dictionary → `O(N)` space.
* A variable's value growing does **not** automatically mean its space is `O(N)`.

### 6. Dominant Growth Rate

Ignore constants and lower-order terms.

* `O(2N)` → `O(N)`
* `O(3N + 5)` → `O(N)`
* `O(3N² + 5N + 10)` → `O(N²)`

### 7. Common Python Operation Complexities

**Lists**

* Indexing → `O(1)`
* `append()` → `O(1)` amortized
* `pop()` → `O(1)`
* `insert(0, x)` → `O(N)`
* `pop(0)` → `O(N)`
* Searching with `in` → `O(N)`
* `remove()` → `O(N)`

**Dictionaries — average case**

* Lookup → `O(1)`
* Insert/update → `O(1)`
* Delete → `O(1)`
* Key existence → `O(1)`
* `.get()` → `O(1)`

### 8. Backend Applications

* Searching users in a list → `O(N)`
* Looking up users by ID in a dictionary → `O(1)` average
* Building a result list → `O(N)` additional space
* Choosing the correct data structure can significantly affect performance as data scales.

## Hands-on Practice

Practiced analyzing:

* Single loops
* Nested loops
* Sequential loops
* Different input sizes
* Search functions
* Functions using growing result lists
* Functions using fixed variables
* Combined time and space complexity
* Backend-oriented user/session examples

## Key Takeaways

* One loop → usually `O(N)`
* Nested loops → usually `O(N²)`
* Two different collections → potentially `O(N × M)`
* Sequential operations add; nested operations multiply.
* Growing storage → `O(N)` space.
* Fixed number of variables → `O(1)` space.
* `return` does not automatically mean extra space.
* A variable whose **value** grows is not necessarily using growing memory.
* Always identify the dominant growth rate.

## Final Competency

Analyzed backend-style functions involving:

* User searches
* Active-user filtering
* Sequential and nested loops
* List-based lookups
* Best/worst-case behavior
* Time and space trade-offs



# Phase 2 — Trees & Trade-Off Defense

## Topics Covered

### 1. Trees (Basic)

* Trees are **non-linear data structures** used to represent hierarchical relationships.
* Learned the basic tree components:

  * Root
  * Parent
  * Child
  * Leaf
  * Edge
* Learned **Binary Trees**:

  * Each node can have at most two children.
  * Left child and right child.
* Learned **Binary Search Trees (BSTs)**:

  * Smaller values → left
  * Larger values → right
* Learned tree traversal:

  * Inorder → Left → Root → Right
  * Preorder → Root → Left → Right
  * Postorder → Left → Right → Root
* Learned basic BST operations:

  * Search
  * Insertion
  * Deletion concepts
* Learned BST complexity:

  * Balanced BST → `O(log N)` for search/insert/delete
  * Unbalanced BST → `O(N)` worst case
* Learned Python representation using a `Node` with:

  * `data`
  * `left`
  * `right`
* Connected trees to real-world systems:

  * Database indexes
  * DOM trees
  * Hierarchical data

## Hands-on Practice

Built a BST in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Constructed:

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

Implemented BST search and inorder traversal.

Search results:

* `60` → `True`
* `100` → `False`

Inorder traversal:

```text
20 30 40 50 60 70 80
```

## 2. Trade-Off Defense

### Scenario

Compared storing user sessions using:

* Array/List
* Hash Map/Dictionary

### Decision

Used a **Hash Map/Dictionary** for session lookup by user ID.

### Reasoning

* List lookup → **O(N)** in the worst case.
* Dictionary lookup → **O(1) average**.
* With a growing number of users, List lookup cost grows linearly.
* Dictionary lookup remains O(1) on average.

### Competency Defense

> "I chose the Hash Map because looking up a user session by ID has an average time complexity of O(1). With an Array/List, lookup can take O(N) because we may need to search through the users one by one. As the number of users increases, the List lookup cost grows linearly, while the Dictionary provides average O(1) lookup. This makes the Hash Map more suitable for session lookups in the backend."

## Key Takeaways

* Trees represent **hierarchical data**.
* BSTs organize values using **left/right ordering**.
* Inorder traversal of a BST produces **sorted values**.
* Balanced BST operations can be **O(log N)**.
* Poorly balanced BSTs can become **O(N)**.
* Choosing the right data structure affects backend performance as data scales.
* Hash Maps are suitable for direct ID-based lookups because they provide **O(1) average lookup**.



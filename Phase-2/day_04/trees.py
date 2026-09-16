"""Build a Binary Search Tree in Python from scratch.

Requirements

Create a Node class with:

data
left
right

Then create a BST containing:

50, 30, 70, 20, 40, 60, 80

Your program should:

Create the nodes and construct the BST.
Search for 60.
Search for 100.
Perform an inorder traversal and print the result.
Expected structure
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
Expected results
60 found
100 not found

Inorder:
20 30 40 50 60 70 80Here's a Python implementation of a Binary Search Tree (BST) that meets your requirements:```python"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

def search(node, key):
    if node is None:
        return False
    if node.data == key:
        return True
    elif key < node.data:
        return search(node.left, key)
    else:
        return search(node.right, key)
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)

print(search(root, 60))
print(search(root, 100))
inorder(root)


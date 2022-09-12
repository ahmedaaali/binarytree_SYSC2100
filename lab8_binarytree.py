# Ahmed Ali (101181126)
# SYSC 2100 Lab 8

"""Class BinaryTree implements the basic binary tree from Section 6.1 of
'Open Data Structures (in pseudocode)', Edition 0.1G Beta.

This module was adapted from code from the Open Data Structures project,
opendatastructures.org.

This code (and the code from which it was derived) is released under a
Creative Commons Attribution (CC BY) license. The full text of the license is
available here:

http://creativecommons.org/licenses/by/2.5/ca/
"""
from typing import Any

__author__ = 'bailey'
__version__ = '1.01'
__date__ = 'Mar. 14, 2022'

# History
# 1.00 Mar. 13, 2022 - Initial release.
# 1.01 Mar. 14, 2022 - Updated type annotations.

class BinaryTree:

    class Node:
        def __init__(self, x: Any) -> None:
            """Construct a node with no parent and no children,
            containing payload x.
            """
            self._x = x
            self._parent = None
            self._left = None
            self._right = None

        def get_left_child(self) -> 'Node':
            """Return the left child of this node."""
            return self._left

        def set_left_child(self, left_child: 'Node') -> None:
            """Replace the left child of this node with left_child."""
            self._left = left_child
            left_child._parent = self

        def get_right_child(self) -> 'Node':
            """Return the right child of this node."""
            return self._right

        def set_right_child(self, right_child: 'Node') -> None:
            """Replace the left child of this node with right_child."""
            self._right = right_child
            right_child._parent = self

    def __init__(self) -> None:
        """Initialize self as an empty BinaryTree."""
        self._root = None

    def set_root(self, node: 'BinaryTree.Node') -> None:
        """Set the root of this binary tree to node."""
        self._root = node

    def get_root(self) -> 'BinaryTree.Node':
        """Return a reference to this binary tree's root node."""
        return self._root

    def depth(self, u: 'BinaryTree.Node') -> int:
        """Return the length of the path from node u to the root of this
        binary tree.
        """
        # Count the steps on the path from u to the root.
        steps = 0
        while u is not self._root:
            u = u._parent
            steps += 1
        return steps

    def traverse(self) -> None:
        """Visit all the nodes in this binary tree."""
        # Recursive implementation.
        self._traverse(self._root)

    def _traverse(self, u: 'BinaryTree.Node') -> None:
        """Visit all the nodes in the binary tree rooted at u.
        """
        if u is None:
            return
        self._traverse(u._left)
        self._traverse(u._right)

    def size(self) -> int:
        """Return the number of nodes in this tree."""
        # Recursive implementation.
        return self._size(self._root)

    def _size(self, u: 'BinaryTree.Node') -> int:
        """Return the number of nodes in the tree rooted at node u."""
        if u is None:
            return 0
        return 1 + self._size(u._left) + self._size(u._right)

    def height(self) -> int:
        """Return the length of the longest path from this tree's root
        to one of its descendants.
        """
        # Recursive implementation
        return self._height(self._root)

    def _height(self, u: 'BinaryTree.Node') -> int:
        """Return the length of the longest path from node u
        to one of its descendants.
        """
        if u is None:
            return -1
        return 1 + max(self._height(u._left), self._height(u._right))

    # Exercise 3

    def preorder_print(self) -> None:
        """Print this binary tree using a preorder traversal."""
        self._preorder_print(self._root)

    def _preorder_print(self, node: 'BinaryTree.Node') -> None:
        """Print the binary tree rooted at node using a preorder traversal."""
        if node is None:
            return
        print(node._x)
        self._preorder_print(node._left)
        self._preorder_print(node._right)

    # Exercise 4

    def inorder_print(self) -> None:
        """Print this binary tree using an inorder traversal."""
        self._inorder_print(self._root)

    def _inorder_print(self, node: 'BinaryTree.Node') -> None:
        """Print the binary tree rooted at node using an inorder traversal."""
        if node is None:
            return
        self._inorder_print(node._left)
        print(node._x)
        self._inorder_print(node._right)

    # Exercise 5

    def postorder_print(self) -> None:
        """Print this binary tree using a postorder traversal."""
        self._postorder_print(self._root)

    def _postorder_print(self, node: 'BinaryTree.Node') -> None:
        """Print the binary tree rooted at node using a postorder traversal."""
        if node is None:
            return
        self._postorder_print(node._left)
        self._postorder_print(node._right)
        print(node._x)

    # Exercise 6

    def count(self, item: Any) -> int:
        """Return the number of occurrences of item in this binary tree."""
        return self._count(self._root, item)

    def _count(self, node: 'BinaryTree.Node', item: Any) -> int:
        """Return the number of occurrences of item in this binary tree rooted at node."""
        if node is None:
            return 0
        if node._x == item:
            return 1 + self._count(node._left, item) + self._count(node._right, item)
        return 0 + self._count(node._left, item) + self._count(node._right, item)

# Exercise 1


def build_binary_tree() -> BinaryTree:
    """Build the binary tree shown in Exercise 1 in the lab handout,
    and return the reference to the tree.
    """
    tree = BinaryTree()
    tree.set_root(BinaryTree.Node(5))
    root0 = tree.get_root()
    root0.set_left_child(BinaryTree.Node(7))
    root0.set_right_child(BinaryTree.Node(12))
    root1 = root0.get_left_child()
    root2 = root0.get_right_child()
    root1.set_left_child(BinaryTree.Node(17))
    root1.set_right_child(BinaryTree.Node(9))
    root2.set_right_child(BinaryTree.Node(6))
    root3 = root2.get_right_child()
    root3.set_left_child(BinaryTree.Node(1))
    return tree

# Exercise 2


def build_full_binary_tree() -> BinaryTree:
    """Build the full binary tree shown in Exercise 2 in the lab handout,
    and return the reference to the tree.
    """
    tree = BinaryTree()
    tree.set_root(BinaryTree.Node(5))
    root0 = tree.get_root()
    root0.set_left_child(BinaryTree.Node(7))
    root0.set_right_child(BinaryTree.Node(12))
    root1 = root0.get_left_child()
    root2 = root0.get_right_child()
    root1.set_left_child(BinaryTree.Node(17))
    root1.set_right_child(BinaryTree.Node(9))
    root2.set_left_child(BinaryTree.Node(3))
    root2.set_right_child(BinaryTree.Node(6))
    return tree


if __name__ == '__main__':
    tree = build_binary_tree()
    print(tree.size())
    tree = build_binary_tree()
    print(tree.count(17))
    # tree.postorder_print()
    tree = build_full_binary_tree()
    # tree.postorder_print()
    print(tree.count(17))

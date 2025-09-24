# tree_node.py

from typing import List, Optional

class TreeNode:
    def __init__(
        self,
        name: Optional[str] = None,              # <-- NEW
        value: Optional[int] = None,
        children: Optional[List['TreeNode']] = None,
        is_max: bool = False,
        leaf_id: Optional[int] = None
    ):
        """
        A node for Minimax/Alpha-Beta trees.
        :param name: Optional human-readable name (e.g., 'A', 'B', or board state for Tic-Tac-Toe)
        :param value: Value for a leaf node (None for internal nodes)
        :param children: List of child TreeNodes (empty list for leaves)
        :param is_max: True if this is a Max node, False if Min node
        :param leaf_id: Optional identifier for leaf (for tracing)
        """
        self.name = name
        self.value = value
        self.children = children if children is not None else []
        self.is_max = is_max
        self.leaf_id = leaf_id

    def is_leaf(self) -> bool:
        """Return True if this is a leaf node (no children)."""
        return len(self.children) == 0

    def add_child(self, child: 'TreeNode'):
        """Append a child to this node."""
        self.children.append(child)

    def __repr__(self):
        if self.is_leaf():
            return f"Leaf(name={self.name}, id={self.leaf_id}, value={self.value})"
        node_type = "Max" if self.is_max else "Min"
        return f"{node_type}Node(name={self.name}, children={len(self.children)})"

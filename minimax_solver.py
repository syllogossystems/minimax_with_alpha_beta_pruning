"""
minimax_solver.py
Minimax implementation that counts leaf evaluations and also returns the chosen path.
Expose:
  - minimax(root) -> (value, path)
  - get_leaf_evals() -> int
  - reset_counter()
"""

from tree_node import TreeNode  # use the shared class

_leaf_evals = 0

def reset_counter():
    global _leaf_evals
    _leaf_evals = 0

def get_leaf_evals():
    return _leaf_evals

def minimax(node: TreeNode):
    """
    Returns:
      (value, path) where
        - value: minimax score
        - path: list of node names/values from root to the chosen leaf
    """
    global _leaf_evals

    # Leaf node
    if not node.children:
        _leaf_evals += 1
        return node.value, [str(node.value)]  # path is just the value

    if node.is_max:
        best_value = float('-inf')
        best_path = []
        for child in node.children:
            child_value, child_path = minimax(child)
            if child_value > best_value:
                best_value = child_value
                # prepend this node's name to the path
                best_path = [node.name or "Max"] + child_path
        return best_value, best_path
    else:  # Min node
        best_value = float('inf')
        best_path = []
        for child in node.children:
            child_value, child_path = minimax(child)
            if child_value < best_value:
                best_value = child_value
                best_path = [node.name or "Min"] + child_path
        return best_value, best_path

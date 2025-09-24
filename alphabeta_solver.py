"""
alphabeta_solver.py

Minimax with Alpha-Beta pruning that:
 - counts leaf evaluations
 - returns chosen path (root -> ... -> leaf)
 - records which leaf_ids were pruned (not evaluated) due to pruning

Public:
 - alphabeta(root) -> (value, path_list)
 - reset_counter()
 - get_leaf_evals() -> int
 - get_pruned_leaf_ids() -> List[int]
"""

from typing import List, Tuple
from tree_node import TreeNode

_leaf_evals = 0
_pruned_leaf_ids = set()

def reset_counter() -> None:
    """Reset leaf-eval counter and cleared pruned set."""
    global _leaf_evals, _pruned_leaf_ids
    _leaf_evals = 0
    _pruned_leaf_ids = set()

def get_leaf_evals() -> int:
    return _leaf_evals

def get_pruned_leaf_ids() -> List[int]:
    """Return sorted list of leaf_ids that were pruned (not evaluated)."""
    return sorted(list(_pruned_leaf_ids))

def _collect_leaf_ids(subtree_root: TreeNode) -> List[int]:
    """
    Recursively collect all leaf_id values under subtree_root.
    If a leaf has no leaf_id, it is ignored.
    """
    collected: List[int] = []
    if subtree_root.is_leaf():
        if getattr(subtree_root, "leaf_id", None) is not None:
            collected.append(subtree_root.leaf_id)
        return collected
    for child in subtree_root.children:
        collected.extend(_collect_leaf_ids(child))
    return collected

def alphabeta(node: TreeNode, alpha: float = float("-inf"), beta: float = float("inf")) -> Tuple[int, List[str]]:
    """
    Run alpha-beta on `node`.
    Returns: (value, path) where path is list of node names/leaf values from root->chosen leaf.
    Also updates global counters and pruned leaf id set.
    """
    global _leaf_evals, _pruned_leaf_ids

    # Leaf node: evaluate
    if node.is_leaf():
        _leaf_evals += 1
        # path is just the leaf value (string)
        return node.value, [str(node.value)]

    # Max node
    if node.is_max:
        best_value = float("-inf")
        best_path: List[str] = []
        # iterate children left-to-right
        child_count = len(node.children)
        for child_index, child_node in enumerate(node.children):
            child_value, child_path = alphabeta(child_node, alpha, beta)
            if child_value > best_value:
                best_value = child_value
                best_path = [node.name or "Max"] + child_path
            # update alpha
            if best_value > alpha:
                alpha = best_value
            # pruning: if alpha >= beta, remaining children are pruned
            if alpha >= beta:
                # collect leaf ids from remaining children (child_index+1 .. end)
                for remaining_child in node.children[child_index + 1:]:
                    pruned_ids = _collect_leaf_ids(remaining_child)
                    _pruned_leaf_ids.update(pruned_ids)
                break
        return best_value, best_path

    # Min node
    else:
        best_value = float("inf")
        best_path: List[str] = []
        child_count = len(node.children)
        for child_index, child_node in enumerate(node.children):
            child_value, child_path = alphabeta(child_node, alpha, beta)
            if child_value < best_value:
                best_value = child_value
                best_path = [node.name or "Min"] + child_path
            # update beta
            if best_value < beta:
                beta = best_value
            # pruning: if beta <= alpha, remaining children are pruned
            if beta <= alpha:
                for remaining_child in node.children[child_index + 1:]:
                    pruned_ids = _collect_leaf_ids(remaining_child)
                    _pruned_leaf_ids.update(pruned_ids)
                break
        return best_value, best_path

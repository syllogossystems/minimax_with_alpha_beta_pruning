# main.py
# Main driver: builds tree using build_tree_by_names and then exposes the root_node for use.
from input_tree import get_input_tree
from tree_print_utils import print_tree_ascii
from minimax_solver import get_leaf_evals, minimax, reset_counter
from alphabeta_solver import reset_counter as alpha_beta_reset_counter, alphabeta, get_leaf_evals as get_alpha_beta_leaf_evals , get_pruned_leaf_ids


if __name__ == "__main__":
    root = get_input_tree()
    print_tree_ascii(root_node=root)
    
    reset_counter()
    value, path = minimax(root)

    print("------------------------ MinMax -------------------")
    print("Minimax result:", value)
    print("Leaf evaluations:", get_leaf_evals())
    print("Chosen path:", " -> ".join(path))


    print("------- MinMax with Alpha Beta Purning --------------")
    alpha_beta_reset_counter()
    alpha_beta_value, alpha_beta_path = alphabeta(root)
    print("Alpha-Beta value:", alpha_beta_value)
    print("Alpha-Beta path:", " -> ".join(alpha_beta_path))
    print("Alpha-Beta leaf evaluations:", get_alpha_beta_leaf_evals())
    print("Pruned leaf ids:", get_pruned_leaf_ids())
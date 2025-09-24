from tree_node import TreeNode

def print_tree_ascii(root_node: TreeNode) -> None:
    """
    Print a human-friendly ASCII tree.
    Internal nodes show their name + [Max/Min].
    Leaf nodes show only their value.
    """

    def format_node_label(node: TreeNode) -> str:
        if node.is_leaf():
            return str(node.value)   # <-- only value, no name
        else:
            name_part = node.name if node.name else ("Max" if node.is_max else "Min")
            role = "Max" if node.is_max else "Min"
            return f"{name_part} [{role}]"

    def recurse(node: TreeNode, prefix: str, is_last_child: bool) -> None:
        line_prefix = prefix + ("└─ " if is_last_child else "├─ ")
        print(line_prefix + format_node_label(node))

        if node.children:
            new_prefix = prefix + ("   " if is_last_child else "│  ")
            child_count = len(node.children)
            for child_index, child_node in enumerate(node.children):
                child_is_last = (child_index == child_count - 1)
                recurse(child_node, new_prefix, child_is_last)

    # Print root without connector
    print(format_node_label(root_node))
    child_count_root = len(root_node.children)
    for index, child in enumerate(root_node.children):
        is_last = (index == child_count_root - 1)
        recurse(child, "", is_last)

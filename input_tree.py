from tree_node import TreeNode

def get_input_tree():
    root = TreeNode(name="A", is_max=True)

    child_b = TreeNode(name="B", is_max=False)
    child_c = TreeNode(name="C", is_max=False)
    root.add_child(child=child_b)
    root.add_child(child=child_c)

    # Level 2 under B
    child_d = TreeNode(name="D", is_max=True)
    child_e = TreeNode(name="E", is_max=True)
    child_b.add_child(child=child_d)
    child_b.add_child(child=child_e)

    # Level 2 under C
    child_f = TreeNode(name="F", is_max=True)
    child_g = TreeNode(name="G", is_max=True)
    child_c.add_child(child=child_f)
    child_c.add_child(child=child_g)

    # Level 3 under D
    child_h = TreeNode(name="H", is_max=False)
    child_i = TreeNode(name="I", is_max=False)
    child_d.add_child(child=child_h)
    child_d.add_child(child=child_i)

    # Level 3 under E
    child_j = TreeNode(name="J", is_max=False)
    child_k = TreeNode(name="K", is_max=False)
    child_e.add_child(child=child_j)
    child_e.add_child(child=child_k)

    # Level 3 under F
    child_l = TreeNode(name="L", is_max=False)
    child_m = TreeNode(name="M", is_max=False)
    child_f.add_child(child=child_l)
    child_f.add_child(child=child_m)

    # Level 3 under G
    child_n = TreeNode(name="N", is_max=False)
    child_o = TreeNode(name="O", is_max=False)   # Stop here as requested
    child_g.add_child(child=child_n)
    child_g.add_child(child=child_o)

        # ---- Add leaves at Level 4 (2 under each H..O) ----
    leaf_id = 0

    # Under H
    child_h.add_child(TreeNode(value=3, leaf_id=leaf_id)); leaf_id += 1
    child_h.add_child(TreeNode(value=5, leaf_id=leaf_id)); leaf_id += 1

    # Under I
    child_i.add_child(TreeNode(value=2, leaf_id=leaf_id)); leaf_id += 1
    child_i.add_child(TreeNode(value=9, leaf_id=leaf_id)); leaf_id += 1

    # Under J
    child_j.add_child(TreeNode(value=7, leaf_id=leaf_id)); leaf_id += 1
    child_j.add_child(TreeNode(value=4, leaf_id=leaf_id)); leaf_id += 1

    # Under K
    child_k.add_child(TreeNode(value=6, leaf_id=leaf_id)); leaf_id += 1
    child_k.add_child(TreeNode(value=1, leaf_id=leaf_id)); leaf_id += 1

    # Under L
    child_l.add_child(TreeNode(value=8, leaf_id=leaf_id)); leaf_id += 1
    child_l.add_child(TreeNode(value=0, leaf_id=leaf_id)); leaf_id += 1

    # Under M
    child_m.add_child(TreeNode(value=10, leaf_id=leaf_id)); leaf_id += 1
    child_m.add_child(TreeNode(value=2, leaf_id=leaf_id)); leaf_id += 1

    # Under N
    child_n.add_child(TreeNode(value=11, leaf_id=leaf_id)); leaf_id += 1
    child_n.add_child(TreeNode(value=12, leaf_id=leaf_id)); leaf_id += 1

    # Under O
    child_o.add_child(TreeNode(value=4, leaf_id=leaf_id)); leaf_id += 1
    child_o.add_child(TreeNode(value=6, leaf_id=leaf_id)); leaf_id += 1

    return root
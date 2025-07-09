"""Lowest Common Ancestor in Binary Search Tree."""

def lowest_common_ancestor(root, p_val, q_val):
    cur = root
    while cur:
        if p_val < cur.key and q_val < cur.key:
            cur = cur.left
        elif p_val > cur.key and q_val > cur.key:
            cur = cur.right
        else:
            return cur.key
    return None

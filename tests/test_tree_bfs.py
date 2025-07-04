from data_structures.bst import BST
from data_structures.tree_bfs import level_order_traversal

def test_level_order():
    t = BST()
    for k in [4, 2, 6, 1, 3]: t.insert(k)
    assert level_order_traversal(t.root) == [[4], [2, 6], [1, 3]]

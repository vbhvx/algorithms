from data_structures.bst import BST
from data_structures.bst_lca import lowest_common_ancestor

def test_lca():
    t = BST()
    for k in [6, 2, 8, 0, 4, 7, 9]: t.insert(k)
    assert lowest_common_ancestor(t.root, 2, 8) == 6
    assert lowest_common_ancestor(t.root, 2, 4) == 2

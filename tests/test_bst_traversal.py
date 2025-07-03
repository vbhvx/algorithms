from data_structures.bst import BST
from data_structures.bst_traversal import inorder_traversal, preorder_traversal

def test_traversals():
    t = BST()
    for k in [4, 2, 6, 1, 3]: t.insert(k)
    assert inorder_traversal(t.root) == [1, 2, 3, 4, 6]
    assert preorder_traversal(t.root) == [4, 2, 1, 3, 6]

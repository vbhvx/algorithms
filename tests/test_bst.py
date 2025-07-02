from data_structures.bst import BST

def test_bst():
    tree = BST()
    tree.insert(5, "five"); tree.insert(3, "three"); tree.insert(8, "eight")
    assert tree.search(5) == "five"
    assert tree.search(3) == "three"
    assert tree.search(10) is None

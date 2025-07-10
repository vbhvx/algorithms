from data_structures.avl_tree import AVLTree

def test_avl():
    avl = AVLTree(); root = None
    for k in [10, 20, 30, 40, 50, 25]: root = avl.insert(root, k)
    assert root.key == 30
    assert avl._height(root) <= 4

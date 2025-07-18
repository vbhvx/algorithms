from data_structures.fenwick_tree import FenwickTree

def test_fenwick_tree():
    ft = FenwickTree(5)
    ft.add(1, 3); ft.add(2, 2); ft.add(3, -1); ft.add(4, 6); ft.add(5, 5)
    assert ft.query(3) == 4
    assert ft.range_query(2, 4) == 7

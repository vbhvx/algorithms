from algorithms.sorting.quick_sort_3way import quick_sort_3way

def test_quick_sort_3way():
    arr = [2, 0, 2, 1, 1, 0]
    assert quick_sort_3way(arr) == [0, 0, 1, 1, 2, 2]

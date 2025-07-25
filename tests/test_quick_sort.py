from algorithms.sorting.quick_sort import quick_sort

def test_quick_sort():
    arr = [10, 7, 8, 9, 1, 5]
    assert quick_sort(arr) == [1, 5, 7, 8, 9, 10]

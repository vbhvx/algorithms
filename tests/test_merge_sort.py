from algorithms.sorting.merge_sort import merge_sort

def test_merge_sort():
    arr = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(arr) == sorted(arr)

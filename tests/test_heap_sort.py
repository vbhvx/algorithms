from algorithms.sorting.heap_sort import heap_sort

def test_heap_sort():
    arr = [12, 11, 13, 5, 6, 7]
    assert heap_sort(arr) == [5, 6, 7, 11, 12, 13]

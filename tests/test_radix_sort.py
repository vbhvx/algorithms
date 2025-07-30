from algorithms.sorting.radix_sort import radix_sort

def test_radix_sort():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    assert radix_sort(arr) == sorted([170, 45, 75, 90, 802, 24, 2, 66])

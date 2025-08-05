from algorithms.searching.median_arrays import find_median_sorted_arrays

def test_median():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

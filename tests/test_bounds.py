from algorithms.searching.bounds import lower_bound, upper_bound

def test_bounds():
    arr = [1, 2, 4, 4, 4, 5, 8]
    assert lower_bound(arr, 4) == 2
    assert upper_bound(arr, 4) == 5

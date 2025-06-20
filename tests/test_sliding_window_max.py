from data_structures.sliding_window_max import max_sliding_window

def test_sliding_window_max():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert max_sliding_window(nums, 3) == [3, 3, 5, 5, 6, 7]

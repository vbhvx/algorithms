from algorithms.searching.search_rotated import search_rotated

def test_search_rotated():
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated(nums, 0) == 4
    assert search_rotated(nums, 3) == -1

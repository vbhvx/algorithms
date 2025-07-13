from data_structures.top_k import top_k_frequent

def test_top_k():
    nums = [1, 1, 1, 2, 2, 3]
    assert set(top_k_frequent(nums, 2)) == {1, 2}

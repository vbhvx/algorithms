from data_structures.subarray_sum import subarray_sum_k

def test_subarray_sum():
    assert subarray_sum_k([1, 1, 1], 2) == 2
    assert subarray_sum_k([1, 2, 3], 3) == 2

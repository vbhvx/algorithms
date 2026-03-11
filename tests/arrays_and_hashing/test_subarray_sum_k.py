"""Unit test suite for Subarray Sum Equals K Prefix Map."""
from src.arrays_and_hashing.subarray_sum_k import SubarraySumEqualsKPrefixMap

def test_subarray_sum_k_basic():
    solver = SubarraySumEqualsKPrefixMap()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_subarray_sum_k_repeated():
    solver = SubarraySumEqualsKPrefixMap()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

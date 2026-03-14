"""Unit test suite for Subarray Sums Divisible by K."""
from src.arrays_and_hashing.subarray_divisible_k import SubarraySumsDivisibleByK

def test_subarray_divisible_k_basic():
    solver = SubarraySumsDivisibleByK()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_subarray_divisible_k_repeated():
    solver = SubarraySumsDivisibleByK()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

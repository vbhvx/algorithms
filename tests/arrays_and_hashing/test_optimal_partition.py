"""Unit test suite for Optimal Partition of String."""
from src.arrays_and_hashing.optimal_partition import OptimalPartitionOfString

def test_optimal_partition_basic():
    solver = OptimalPartitionOfString()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_optimal_partition_repeated():
    solver = OptimalPartitionOfString()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

"""Unit test suite for Top K Frequent Elements Bucket Sort."""
from src.arrays_and_hashing.top_k_frequent import TopKFrequentElementsBucketSort

def test_top_k_frequent_basic():
    solver = TopKFrequentElementsBucketSort()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_top_k_frequent_repeated():
    solver = TopKFrequentElementsBucketSort()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

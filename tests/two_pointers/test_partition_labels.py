"""Unit test suite for Partition Labels Last Seen Index."""
from src.two_pointers.partition_labels import PartitionLabelsLastSeenIndex

def test_partition_labels_basic():
    solver = PartitionLabelsLastSeenIndex()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_partition_labels_repeated():
    solver = PartitionLabelsLastSeenIndex()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

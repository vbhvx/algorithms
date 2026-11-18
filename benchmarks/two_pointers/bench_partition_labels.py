"""Benchmark profile for Partition Labels Last Seen Index."""
import time
from src.two_pointers.partition_labels import PartitionLabelsLastSeenIndex

def benchmark():
    solver = PartitionLabelsLastSeenIndex()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    print(f"Execution duration: {benchmark():.6f}s")

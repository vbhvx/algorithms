"""Benchmark profile for Longest Consecutive Sequence Set."""
import time
from src.arrays_and_hashing.longest_consecutive import LongestConsecutiveSequenceSet

def benchmark():
    solver = LongestConsecutiveSequenceSet()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

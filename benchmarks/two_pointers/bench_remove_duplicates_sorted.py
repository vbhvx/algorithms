"""Benchmark profile for Remove Duplicates Sorted Array."""
import time
from src.two_pointers.remove_duplicates_sorted import RemoveDuplicatesSortedArray

def benchmark():
    solver = RemoveDuplicatesSortedArray()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

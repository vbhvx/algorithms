"""Benchmark profile for Remove Duplicates Sorted Array II."""
import time
from src.two_pointers.remove_duplicates_ii import RemoveDuplicatesSortedArrayIi

def benchmark():
    solver = RemoveDuplicatesSortedArrayIi()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

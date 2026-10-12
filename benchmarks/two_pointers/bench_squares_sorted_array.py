"""Benchmark profile for Squares of Sorted Array."""
import time
from src.two_pointers.squares_sorted_array import SquaresOfSortedArray

def benchmark():
    solver = SquaresOfSortedArray()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

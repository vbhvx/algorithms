"""Benchmark profile for Backspace String Compare Reverse."""
import time
from src.two_pointers.backspace_compare import BackspaceStringCompareReverse

def benchmark():
    solver = BackspaceStringCompareReverse()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

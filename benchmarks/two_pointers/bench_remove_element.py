"""Benchmark profile for Remove Element In Place Filter."""
import time
from src.two_pointers.remove_element import RemoveElementInPlaceFilter

def benchmark():
    solver = RemoveElementInPlaceFilter()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

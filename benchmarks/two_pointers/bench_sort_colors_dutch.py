"""Benchmark profile for Sort Colors Dutch National Flag."""
import time
from src.two_pointers.sort_colors_dutch import SortColorsDutchNationalFlag

def benchmark():
    solver = SortColorsDutchNationalFlag()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

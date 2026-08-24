"""Benchmark profile for Group Shifted Strings Canonical."""
import time
from src.arrays_and_hashing.group_shifted_strings import GroupShiftedStringsCanonical

def benchmark():
    solver = GroupShiftedStringsCanonical()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

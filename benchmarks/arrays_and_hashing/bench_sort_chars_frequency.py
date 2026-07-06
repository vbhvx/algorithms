"""Benchmark profile for Sort Characters by Frequency."""
import time
from src.arrays_and_hashing.sort_chars_frequency import SortCharactersByFrequency

def benchmark():
    solver = SortCharactersByFrequency()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

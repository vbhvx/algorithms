"""Benchmark profile for Valid Anagram Counter."""
import time
from src.arrays_and_hashing.valid_anagram import ValidAnagramCounter

def benchmark():
    solver = ValidAnagramCounter()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

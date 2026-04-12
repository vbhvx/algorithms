"""Benchmark profile for Find All Anagrams Sliding Window."""
import time
from src.arrays_and_hashing.find_all_anagrams import FindAllAnagramsSlidingWindow

def benchmark():
    solver = FindAllAnagramsSlidingWindow()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

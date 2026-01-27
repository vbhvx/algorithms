"""Benchmark profile for Group Anagrams Sorted Key."""
import time
from src.arrays_and_hashing.group_anagrams import GroupAnagramsSortedKey

def benchmark():
    solver = GroupAnagramsSortedKey()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

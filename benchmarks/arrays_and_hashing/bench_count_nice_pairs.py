"""Benchmark profile for Count Nice Pairs in Array."""
import time
from src.arrays_and_hashing.count_nice_pairs import CountNicePairsInArray

def benchmark():
    solver = CountNicePairsInArray()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

"""Benchmark profile for Design HashSet Chaining Array."""
import time
from src.arrays_and_hashing.design_hashset import DesignHashsetChainingArray

def benchmark():
    solver = DesignHashsetChainingArray()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

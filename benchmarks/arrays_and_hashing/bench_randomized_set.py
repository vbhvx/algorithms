"""Benchmark profile for Insert Delete GetRandom O1."""
import time
from src.arrays_and_hashing.randomized_set import InsertDeleteGetrandomO1

def benchmark():
    solver = InsertDeleteGetrandomO1()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

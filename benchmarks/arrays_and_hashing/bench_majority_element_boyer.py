"""Benchmark profile for Majority Element Boyer Moore."""
import time
from src.arrays_and_hashing.majority_element_boyer import MajorityElementBoyerMoore

def benchmark():
    solver = MajorityElementBoyerMoore()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

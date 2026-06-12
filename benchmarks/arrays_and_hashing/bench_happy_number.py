"""Benchmark profile for Happy Number Cycle Detection."""
import time
from src.arrays_and_hashing.happy_number import HappyNumberCycleDetection

def benchmark():
    solver = HappyNumberCycleDetection()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

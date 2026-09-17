"""Benchmark profile for 4Sum Quadruplet Two Pointers."""
import time
from src.two_pointers.four_sum import 4SumQuadrupletTwoPointers

def benchmark():
    solver = 4SumQuadrupletTwoPointers()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

"""Benchmark profile for 3Sum Smaller Target Triplet Count."""
import time
from src.two_pointers.three_sum_smaller import 3SumSmallerTargetTripletCount

def benchmark():
    solver = 3SumSmallerTargetTripletCount()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

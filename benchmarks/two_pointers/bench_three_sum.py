"""Benchmark profile for 3Sum Zero Triplet Two Pointers."""
import time
from src.two_pointers.three_sum import 3SumZeroTripletTwoPointers

def benchmark():
    solver = 3SumZeroTripletTwoPointers()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

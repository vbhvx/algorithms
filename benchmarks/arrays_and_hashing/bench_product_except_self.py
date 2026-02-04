"""Benchmark profile for Product of Array Except Self."""
import time
from src.arrays_and_hashing.product_except_self import ProductOfArrayExceptSelf

def benchmark():
    solver = ProductOfArrayExceptSelf()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

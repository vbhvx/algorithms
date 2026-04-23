"""Benchmark profile for Brick Wall Minimum Cross Cuts."""
import time
from src.arrays_and_hashing.brick_wall import BrickWallMinimumCrossCuts

def benchmark():
    solver = BrickWallMinimumCrossCuts()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

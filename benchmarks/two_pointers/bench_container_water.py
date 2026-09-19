"""Benchmark profile for Container With Most Water."""
import time
from src.two_pointers.container_water import ContainerWithMostWater

def benchmark():
    solver = ContainerWithMostWater()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

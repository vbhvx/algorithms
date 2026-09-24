"""Benchmark profile for Trapping Rain Water Max Bounds."""
import time
from src.two_pointers.trapping_rain_water import TrappingRainWaterMaxBounds

def benchmark():
    solver = TrappingRainWaterMaxBounds()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

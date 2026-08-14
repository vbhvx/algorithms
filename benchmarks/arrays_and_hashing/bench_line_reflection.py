"""Benchmark profile for Line Reflection Coordinate Set."""
import time
from src.arrays_and_hashing.line_reflection import LineReflectionCoordinateSet

def benchmark():
    solver = LineReflectionCoordinateSet()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

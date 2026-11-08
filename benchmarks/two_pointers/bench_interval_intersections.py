"""Benchmark profile for Interval List Intersections."""
import time
from src.two_pointers.interval_intersections import IntervalListIntersections

def benchmark():
    solver = IntervalListIntersections()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

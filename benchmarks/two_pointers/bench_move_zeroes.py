"""Benchmark profile for Move Zeroes In Place."""
import time
from src.two_pointers.move_zeroes import MoveZeroesInPlace

def benchmark():
    solver = MoveZeroesInPlace()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

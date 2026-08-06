"""Benchmark profile for Pairs of Songs Divisible by 60."""
import time
from src.arrays_and_hashing.songs_divisible_60 import PairsOfSongsDivisibleBy60

def benchmark():
    solver = PairsOfSongsDivisibleBy60()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

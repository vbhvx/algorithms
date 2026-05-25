"""Benchmark profile for Word Pattern Bijective Mapping."""
import time
from src.arrays_and_hashing.word_pattern import WordPatternBijectiveMapping

def benchmark():
    solver = WordPatternBijectiveMapping()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")

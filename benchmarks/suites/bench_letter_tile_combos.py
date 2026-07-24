"""
Empirical benchmark for Letter Tile Possibilities Frequency Backtrack
"""
import time
from algorithms.practice.backtracking.letter_tile_combos import solve_letter_tile_combos

def benchmark_letter_tile_combos():
    start = time.perf_counter()
    for _ in range(100):
        solve_letter_tile_combos([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_letter_tile_combos()
    print(f"Letter Tile Possibilities Frequency Backtrack 100 iterations took {t*1000:.3f}ms")

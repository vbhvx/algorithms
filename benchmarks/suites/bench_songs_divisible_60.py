"""
Empirical benchmark for Pairs of Songs Divisible by 60
"""
import time
from algorithms.practice.arrays_and_hashing.songs_divisible_60 import solve_songs_divisible_60

def benchmark_songs_divisible_60():
    start = time.perf_counter()
    for _ in range(100):
        solve_songs_divisible_60([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_songs_divisible_60()
    print(f"Pairs of Songs Divisible by 60 100 iterations took {t*1000:.3f}ms")

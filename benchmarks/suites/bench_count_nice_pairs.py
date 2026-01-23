"""
Empirical benchmark for Count Nice Pairs in Array
"""
import time
from algorithms.practice.arrays_and_hashing.count_nice_pairs import solve_count_nice_pairs

def benchmark_count_nice_pairs():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_nice_pairs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_nice_pairs()
    print(f"Count Nice Pairs in Array 100 iterations took {t*1000:.3f}ms")

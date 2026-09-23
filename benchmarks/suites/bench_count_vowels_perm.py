"""
Empirical benchmark for Count Vowels Permutation Directed Transitions
"""
import time
from algorithms.practice.dynamic_programming_1d.count_vowels_perm import solve_count_vowels_perm

def benchmark_count_vowels_perm():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_vowels_perm([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_vowels_perm()
    print(f"Count Vowels Permutation Directed Transitions 100 iterations took {t*1000:.3f}ms")

"""
Empirical benchmark for Find All Anagrams Sliding Window
"""
import time
from algorithms.practice.arrays_and_hashing.find_all_anagrams import solve_find_all_anagrams

def benchmark_find_all_anagrams():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_all_anagrams([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_all_anagrams()
    print(f"Find All Anagrams Sliding Window 100 iterations took {t*1000:.3f}ms")

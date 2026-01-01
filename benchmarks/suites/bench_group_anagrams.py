"""
Empirical benchmark for Group Anagrams Sorted Key
"""
import time
from algorithms.practice.arrays_and_hashing.group_anagrams import solve_group_anagrams

def benchmark_group_anagrams():
    start = time.perf_counter()
    for _ in range(100):
        solve_group_anagrams([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_group_anagrams()
    print(f"Group Anagrams Sorted Key 100 iterations took {t*1000:.3f}ms")

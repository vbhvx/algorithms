"""
Empirical benchmark for Valid Anagram Counter
"""
import time
from algorithms.practice.arrays_and_hashing.valid_anagram import solve_valid_anagram

def benchmark_valid_anagram():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_anagram([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_anagram()
    print(f"Valid Anagram Counter 100 iterations took {t*1000:.3f}ms")

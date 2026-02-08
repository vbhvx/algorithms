"""
Empirical benchmark for Reverse Vowels of String
"""
import time
from algorithms.practice.two_pointers.reverse_vowels import solve_reverse_vowels

def benchmark_reverse_vowels():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_vowels([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_vowels()
    print(f"Reverse Vowels of String 100 iterations took {t*1000:.3f}ms")

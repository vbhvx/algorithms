"""
Empirical benchmark for Reverse Words in a String III
"""
import time
from algorithms.practice.two_pointers.reverse_words_iii import solve_reverse_words_iii

def benchmark_reverse_words_iii():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_words_iii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_words_iii()
    print(f"Reverse Words in a String III 100 iterations took {t*1000:.3f}ms")

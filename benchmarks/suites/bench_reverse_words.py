"""
Empirical benchmark for Reverse Words in a String In Place
"""
import time
from algorithms.practice.two_pointers.reverse_words import solve_reverse_words

def benchmark_reverse_words():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_words([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_words()
    print(f"Reverse Words in a String In Place 100 iterations took {t*1000:.3f}ms")

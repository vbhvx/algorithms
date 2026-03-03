"""
Empirical benchmark for K Length Substrings No Repeats
"""
import time
from algorithms.practice.sliding_window.k_length_no_repeats import solve_k_length_no_repeats

def benchmark_k_length_no_repeats():
    start = time.perf_counter()
    for _ in range(100):
        solve_k_length_no_repeats([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_k_length_no_repeats()
    print(f"K Length Substrings No Repeats 100 iterations took {t*1000:.3f}ms")

"""
Empirical benchmark for Remove K Digits Peak Element Removal
"""
import time
from algorithms.practice.greedy_algorithms.remove_k_digits_greedy import solve_remove_k_digits_greedy

def benchmark_remove_k_digits_greedy():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_k_digits_greedy([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_k_digits_greedy()
    print(f"Remove K Digits Peak Element Removal 100 iterations took {t*1000:.3f}ms")

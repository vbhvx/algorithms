"""
Empirical benchmark for Find K Closest Elements Window
"""
import time
from algorithms.practice.two_pointers.k_closest_elements import solve_k_closest_elements

def benchmark_k_closest_elements():
    start = time.perf_counter()
    for _ in range(100):
        solve_k_closest_elements([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_k_closest_elements()
    print(f"Find K Closest Elements Window 100 iterations took {t*1000:.3f}ms")

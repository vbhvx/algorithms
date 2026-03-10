"""
Empirical benchmark for Subarrays Max Element K Times
"""
import time
from algorithms.practice.sliding_window.max_element_k_times import solve_max_element_k_times

def benchmark_max_element_k_times():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_element_k_times([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_element_k_times()
    print(f"Subarrays Max Element K Times 100 iterations took {t*1000:.3f}ms")

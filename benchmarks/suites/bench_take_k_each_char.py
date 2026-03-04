"""
Empirical benchmark for Take K Each Character Left Right
"""
import time
from algorithms.practice.sliding_window.take_k_each_char import solve_take_k_each_char

def benchmark_take_k_each_char():
    start = time.perf_counter()
    for _ in range(100):
        solve_take_k_each_char([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_take_k_each_char()
    print(f"Take K Each Character Left Right 100 iterations took {t*1000:.3f}ms")

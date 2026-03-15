"""
Empirical benchmark for Remove K Digits Monotonic Greed
"""
import time
from algorithms.practice.stack_and_queue.remove_k_digits import solve_remove_k_digits

def benchmark_remove_k_digits():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_k_digits([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_k_digits()
    print(f"Remove K Digits Monotonic Greed 100 iterations took {t*1000:.3f}ms")

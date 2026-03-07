"""
Empirical benchmark for Subarrays With Score Less Than K
"""
import time
from algorithms.practice.sliding_window.subarrays_score_less_k import solve_subarrays_score_less_k

def benchmark_subarrays_score_less_k():
    start = time.perf_counter()
    for _ in range(100):
        solve_subarrays_score_less_k([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_subarrays_score_less_k()
    print(f"Subarrays With Score Less Than K 100 iterations took {t*1000:.3f}ms")

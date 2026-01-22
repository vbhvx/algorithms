"""
Empirical benchmark for Logger Rate Limiter Lookup
"""
import time
from algorithms.practice.arrays_and_hashing.logger_rate_limiter import solve_logger_rate_limiter

def benchmark_logger_rate_limiter():
    start = time.perf_counter()
    for _ in range(100):
        solve_logger_rate_limiter([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_logger_rate_limiter()
    print(f"Logger Rate Limiter Lookup 100 iterations took {t*1000:.3f}ms")

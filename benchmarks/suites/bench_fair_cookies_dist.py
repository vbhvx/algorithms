"""
Empirical benchmark for Fair Distribution of Cookies Min Max
"""
import time
from algorithms.practice.backtracking.fair_cookies_dist import solve_fair_cookies_dist

def benchmark_fair_cookies_dist():
    start = time.perf_counter()
    for _ in range(100):
        solve_fair_cookies_dist([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_fair_cookies_dist()
    print(f"Fair Distribution of Cookies Min Max 100 iterations took {t*1000:.3f}ms")

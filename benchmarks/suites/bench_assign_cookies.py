"""
Empirical benchmark for Assign Cookies Greedy Pointers
"""
import time
from algorithms.practice.two_pointers.assign_cookies import solve_assign_cookies

def benchmark_assign_cookies():
    start = time.perf_counter()
    for _ in range(100):
        solve_assign_cookies([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_assign_cookies()
    print(f"Assign Cookies Greedy Pointers 100 iterations took {t*1000:.3f}ms")

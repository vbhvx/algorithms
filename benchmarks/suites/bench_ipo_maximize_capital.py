"""
Empirical benchmark for IPO Maximize Capital Dual Heaps Greed
"""
import time
from algorithms.practice.heaps_and_priority.ipo_maximize_capital import solve_ipo_maximize_capital

def benchmark_ipo_maximize_capital():
    start = time.perf_counter()
    for _ in range(100):
        solve_ipo_maximize_capital([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ipo_maximize_capital()
    print(f"IPO Maximize Capital Dual Heaps Greed 100 iterations took {t*1000:.3f}ms")

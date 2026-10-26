"""
Empirical benchmark for Minimum Number of Arrows to Burst Balloons
"""
import time
from algorithms.practice.greedy_algorithms.min_arrows_burst_balloons import solve_min_arrows_burst_balloons

def benchmark_min_arrows_burst_balloons():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_arrows_burst_balloons([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_arrows_burst_balloons()
    print(f"Minimum Number of Arrows to Burst Balloons 100 iterations took {t*1000:.3f}ms")

"""
Empirical benchmark for Karger-Stein Randomized Contraction Min-Cut
"""
import time
from algorithms.practice.network_flow_matching.karger_stein_mincut import solve_karger_stein_mincut

def benchmark_karger_stein_mincut():
    start = time.perf_counter()
    for _ in range(100):
        solve_karger_stein_mincut([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_karger_stein_mincut()
    print(f"Karger-Stein Randomized Contraction Min-Cut 100 iterations took {t*1000:.3f}ms")

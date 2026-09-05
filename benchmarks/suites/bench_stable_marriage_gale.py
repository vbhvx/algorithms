"""
Empirical benchmark for Gale-Shapley Stable Marriage Matching
"""
import time
from algorithms.practice.network_flow_matching.stable_marriage_gale import solve_stable_marriage_gale

def benchmark_stable_marriage_gale():
    start = time.perf_counter()
    for _ in range(100):
        solve_stable_marriage_gale([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stable_marriage_gale()
    print(f"Gale-Shapley Stable Marriage Matching 100 iterations took {t*1000:.3f}ms")

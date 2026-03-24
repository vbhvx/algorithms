"""
Empirical benchmark for Koko Eating Bananas Capacity Bisect
"""
import time
from algorithms.practice.binary_search.koko_eating_bananas import solve_koko_eating_bananas

def benchmark_koko_eating_bananas():
    start = time.perf_counter()
    for _ in range(100):
        solve_koko_eating_bananas([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_koko_eating_bananas()
    print(f"Koko Eating Bananas Capacity Bisect 100 iterations took {t*1000:.3f}ms")

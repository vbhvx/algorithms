"""
Empirical benchmark for Push-Relabel Algorithm Highest Label Preflow
"""
import time
from algorithms.practice.network_flow_matching.push_relabel_highest import solve_push_relabel_highest

def benchmark_push_relabel_highest():
    start = time.perf_counter()
    for _ in range(100):
        solve_push_relabel_highest([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_push_relabel_highest()
    print(f"Push-Relabel Algorithm Highest Label Preflow 100 iterations took {t*1000:.3f}ms")

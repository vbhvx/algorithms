"""
Empirical benchmark for Accounts Merge Connected Components DSU
"""
import time
from algorithms.practice.graphs_and_traversals.accounts_merge_graph import solve_accounts_merge_graph

def benchmark_accounts_merge_graph():
    start = time.perf_counter()
    for _ in range(100):
        solve_accounts_merge_graph([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_accounts_merge_graph()
    print(f"Accounts Merge Connected Components DSU 100 iterations took {t*1000:.3f}ms")

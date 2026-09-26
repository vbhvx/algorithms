"""
Empirical benchmark for Best Time Stock IV At Most K Transactions
"""
import time
from algorithms.practice.dynamic_programming_2d.stock_k_transactions import solve_stock_k_transactions

def benchmark_stock_k_transactions():
    start = time.perf_counter()
    for _ in range(100):
        solve_stock_k_transactions([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stock_k_transactions()
    print(f"Best Time Stock IV At Most K Transactions 100 iterations took {t*1000:.3f}ms")

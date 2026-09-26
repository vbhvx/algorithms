"""
Empirical benchmark for Best Time Stock with Transaction Fee
"""
import time
from algorithms.practice.dynamic_programming_2d.stock_transaction_fee import solve_stock_transaction_fee

def benchmark_stock_transaction_fee():
    start = time.perf_counter()
    for _ in range(100):
        solve_stock_transaction_fee([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stock_transaction_fee()
    print(f"Best Time Stock with Transaction Fee 100 iterations took {t*1000:.3f}ms")

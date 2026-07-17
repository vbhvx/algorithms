"""
Empirical benchmark for Split Array into Fibonacci Sequence
"""
import time
from algorithms.practice.backtracking.split_fibonacci_seq import solve_split_fibonacci_seq

def benchmark_split_fibonacci_seq():
    start = time.perf_counter()
    for _ in range(100):
        solve_split_fibonacci_seq([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_split_fibonacci_seq()
    print(f"Split Array into Fibonacci Sequence 100 iterations took {t*1000:.3f}ms")

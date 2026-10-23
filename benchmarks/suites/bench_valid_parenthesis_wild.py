"""
Empirical benchmark for Valid Parenthesis String Low High Counters
"""
import time
from algorithms.practice.greedy_algorithms.valid_parenthesis_wild import solve_valid_parenthesis_wild

def benchmark_valid_parenthesis_wild():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_parenthesis_wild([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_parenthesis_wild()
    print(f"Valid Parenthesis String Low High Counters 100 iterations took {t*1000:.3f}ms")

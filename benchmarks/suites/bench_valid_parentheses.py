"""
Empirical benchmark for Valid Parentheses Matcher
"""
import time
from algorithms.practice.stack_and_queue.valid_parentheses import solve_valid_parentheses

def benchmark_valid_parentheses():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_parentheses([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_parentheses()
    print(f"Valid Parentheses Matcher 100 iterations took {t*1000:.3f}ms")

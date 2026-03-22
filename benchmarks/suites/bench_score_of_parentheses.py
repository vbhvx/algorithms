"""
Empirical benchmark for Score of Parentheses Depth Tracking
"""
import time
from algorithms.practice.stack_and_queue.score_of_parentheses import solve_score_of_parentheses

def benchmark_score_of_parentheses():
    start = time.perf_counter()
    for _ in range(100):
        solve_score_of_parentheses([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_score_of_parentheses()
    print(f"Score of Parentheses Depth Tracking 100 iterations took {t*1000:.3f}ms")

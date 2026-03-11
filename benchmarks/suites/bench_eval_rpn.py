"""
Empirical benchmark for Evaluate Reverse Polish Notation
"""
import time
from algorithms.practice.stack_and_queue.eval_rpn import solve_eval_rpn

def benchmark_eval_rpn():
    start = time.perf_counter()
    for _ in range(100):
        solve_eval_rpn([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_eval_rpn()
    print(f"Evaluate Reverse Polish Notation 100 iterations took {t*1000:.3f}ms")

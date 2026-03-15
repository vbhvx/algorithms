"""
Empirical benchmark for 132 Pattern Monotonic Stack Peak
"""
import time
from algorithms.practice.stack_and_queue.pattern_132 import solve_pattern_132

def benchmark_pattern_132():
    start = time.perf_counter()
    for _ in range(100):
        solve_pattern_132([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_pattern_132()
    print(f"132 Pattern Monotonic Stack Peak 100 iterations took {t*1000:.3f}ms")

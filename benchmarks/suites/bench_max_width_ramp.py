"""
Empirical benchmark for Maximum Width Ramp Monotonic Index
"""
import time
from algorithms.practice.stack_and_queue.max_width_ramp import solve_max_width_ramp

def benchmark_max_width_ramp():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_width_ramp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_width_ramp()
    print(f"Maximum Width Ramp Monotonic Index 100 iterations took {t*1000:.3f}ms")

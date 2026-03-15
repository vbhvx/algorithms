"""
Empirical benchmark for Validate Stack Sequences Pop Simulation
"""
import time
from algorithms.practice.stack_and_queue.validate_stack_seq import solve_validate_stack_seq

def benchmark_validate_stack_seq():
    start = time.perf_counter()
    for _ in range(100):
        solve_validate_stack_seq([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_validate_stack_seq()
    print(f"Validate Stack Sequences Pop Simulation 100 iterations took {t*1000:.3f}ms")

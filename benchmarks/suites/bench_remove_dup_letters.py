"""
Empirical benchmark for Remove Duplicate Letters Lexicographical
"""
import time
from algorithms.practice.stack_and_queue.remove_dup_letters import solve_remove_dup_letters

def benchmark_remove_dup_letters():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_dup_letters([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_dup_letters()
    print(f"Remove Duplicate Letters Lexicographical 100 iterations took {t*1000:.3f}ms")

"""
Empirical benchmark for Process Tasks Using Servers Two Heaps
"""
import time
from algorithms.practice.heaps_and_priority.process_tasks_servers import solve_process_tasks_servers

def benchmark_process_tasks_servers():
    start = time.perf_counter()
    for _ in range(100):
        solve_process_tasks_servers([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_process_tasks_servers()
    print(f"Process Tasks Using Servers Two Heaps 100 iterations took {t*1000:.3f}ms")

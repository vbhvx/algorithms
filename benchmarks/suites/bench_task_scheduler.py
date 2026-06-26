"""
Empirical benchmark for Task Scheduler MaxHeap Frequency Math
"""
import time
from algorithms.practice.heaps_and_priority.task_scheduler import solve_task_scheduler

def benchmark_task_scheduler():
    start = time.perf_counter()
    for _ in range(100):
        solve_task_scheduler([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_task_scheduler()
    print(f"Task Scheduler MaxHeap Frequency Math 100 iterations took {t*1000:.3f}ms")

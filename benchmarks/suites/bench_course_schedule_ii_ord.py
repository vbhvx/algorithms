"""
Empirical benchmark for Course Schedule II Ordering Topological
"""
import time
from algorithms.practice.graphs_and_traversals.course_schedule_ii_ord import solve_course_schedule_ii_ord

def benchmark_course_schedule_ii_ord():
    start = time.perf_counter()
    for _ in range(100):
        solve_course_schedule_ii_ord([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_course_schedule_ii_ord()
    print(f"Course Schedule II Ordering Topological 100 iterations took {t*1000:.3f}ms")

"""
Empirical benchmark for Course Schedule IV Reachability Closure
"""
import time
from algorithms.practice.graphs_and_traversals.course_schedule_iv_q import solve_course_schedule_iv_q

def benchmark_course_schedule_iv_q():
    start = time.perf_counter()
    for _ in range(100):
        solve_course_schedule_iv_q([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_course_schedule_iv_q()
    print(f"Course Schedule IV Reachability Closure 100 iterations took {t*1000:.3f}ms")

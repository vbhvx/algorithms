"""
Empirical benchmark for Course Schedule Kahn Topological Sort In-Degree
"""
import time
from algorithms.practice.graphs_and_traversals.course_schedule_topo import solve_course_schedule_topo

def benchmark_course_schedule_topo():
    start = time.perf_counter()
    for _ in range(100):
        solve_course_schedule_topo([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_course_schedule_topo()
    print(f"Course Schedule Kahn Topological Sort In-Degree 100 iterations took {t*1000:.3f}ms")

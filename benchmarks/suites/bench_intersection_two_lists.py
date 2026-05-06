"""
Empirical benchmark for Intersection of Two Linked Lists Pointer Match
"""
import time
from algorithms.practice.linked_lists.intersection_two_lists import solve_intersection_two_lists

def benchmark_intersection_two_lists():
    start = time.perf_counter()
    for _ in range(100):
        solve_intersection_two_lists([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_intersection_two_lists()
    print(f"Intersection of Two Linked Lists Pointer Match 100 iterations took {t*1000:.3f}ms")

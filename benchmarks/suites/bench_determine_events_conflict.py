"""
Empirical benchmark for Determine if Two Events Have Conflict
"""
import time
from algorithms.practice.intervals_scheduling.determine_events_conflict import solve_determine_events_conflict

def benchmark_determine_events_conflict():
    start = time.perf_counter()
    for _ in range(100):
        solve_determine_events_conflict([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_determine_events_conflict()
    print(f"Determine if Two Events Have Conflict 100 iterations took {t*1000:.3f}ms")

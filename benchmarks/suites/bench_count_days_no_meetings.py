"""
Empirical benchmark for Count Days Without Meetings Merged Gaps
"""
import time
from algorithms.practice.intervals_scheduling.count_days_no_meetings import solve_count_days_no_meetings

def benchmark_count_days_no_meetings():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_days_no_meetings([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_days_no_meetings()
    print(f"Count Days Without Meetings Merged Gaps 100 iterations took {t*1000:.3f}ms")

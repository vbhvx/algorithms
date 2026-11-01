"""
Empirical benchmark for My Calendar I Segment Overlap Tree
"""
import time
from algorithms.practice.intervals_scheduling.my_calendar_i_booking import solve_my_calendar_i_booking

def benchmark_my_calendar_i_booking():
    start = time.perf_counter()
    for _ in range(100):
        solve_my_calendar_i_booking([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_my_calendar_i_booking()
    print(f"My Calendar I Segment Overlap Tree 100 iterations took {t*1000:.3f}ms")

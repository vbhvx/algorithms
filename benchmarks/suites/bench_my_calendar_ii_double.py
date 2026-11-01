"""
Empirical benchmark for My Calendar II Double Booking Overlap
"""
import time
from algorithms.practice.intervals_scheduling.my_calendar_ii_double import solve_my_calendar_ii_double

def benchmark_my_calendar_ii_double():
    start = time.perf_counter()
    for _ in range(100):
        solve_my_calendar_ii_double([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_my_calendar_ii_double()
    print(f"My Calendar II Double Booking Overlap 100 iterations took {t*1000:.3f}ms")

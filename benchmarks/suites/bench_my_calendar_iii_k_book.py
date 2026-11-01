"""
Empirical benchmark for My Calendar III Maximum K-Booking Sweep Line
"""
import time
from algorithms.practice.intervals_scheduling.my_calendar_iii_k_book import solve_my_calendar_iii_k_book

def benchmark_my_calendar_iii_k_book():
    start = time.perf_counter()
    for _ in range(100):
        solve_my_calendar_iii_k_book([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_my_calendar_iii_k_book()
    print(f"My Calendar III Maximum K-Booking Sweep Line 100 iterations took {t*1000:.3f}ms")

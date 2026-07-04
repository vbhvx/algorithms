"""
Empirical benchmark for Seat Reservation Manager MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.seat_reservation_mgr import solve_seat_reservation_mgr

def benchmark_seat_reservation_mgr():
    start = time.perf_counter()
    for _ in range(100):
        solve_seat_reservation_mgr([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_seat_reservation_mgr()
    print(f"Seat Reservation Manager MinHeap 100 iterations took {t*1000:.3f}ms")

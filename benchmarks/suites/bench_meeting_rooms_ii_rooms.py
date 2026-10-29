"""
Empirical benchmark for Meeting Rooms II Chronological Sweep MinHeap
"""
import time
from algorithms.practice.intervals_scheduling.meeting_rooms_ii_rooms import solve_meeting_rooms_ii_rooms

def benchmark_meeting_rooms_ii_rooms():
    start = time.perf_counter()
    for _ in range(100):
        solve_meeting_rooms_ii_rooms([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_meeting_rooms_ii_rooms()
    print(f"Meeting Rooms II Chronological Sweep MinHeap 100 iterations took {t*1000:.3f}ms")

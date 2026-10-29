"""
Empirical benchmark for Meeting Rooms Single Room Conflict Check
"""
import time
from algorithms.practice.intervals_scheduling.meeting_rooms_conflict import solve_meeting_rooms_conflict

def benchmark_meeting_rooms_conflict():
    start = time.perf_counter()
    for _ in range(100):
        solve_meeting_rooms_conflict([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_meeting_rooms_conflict()
    print(f"Meeting Rooms Single Room Conflict Check 100 iterations took {t*1000:.3f}ms")

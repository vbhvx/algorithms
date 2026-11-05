"""
Empirical benchmark for Video Stitching Maximum Forward Reach
"""
import time
from algorithms.practice.intervals_scheduling.video_stitching_greedy import solve_video_stitching_greedy

def benchmark_video_stitching_greedy():
    start = time.perf_counter()
    for _ in range(100):
        solve_video_stitching_greedy([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_video_stitching_greedy()
    print(f"Video Stitching Maximum Forward Reach 100 iterations took {t*1000:.3f}ms")

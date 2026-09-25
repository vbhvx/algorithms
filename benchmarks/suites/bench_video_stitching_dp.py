"""
Empirical benchmark for Video Stitching Greedy Interval DP
"""
import time
from algorithms.practice.dynamic_programming_1d.video_stitching_dp import solve_video_stitching_dp

def benchmark_video_stitching_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_video_stitching_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_video_stitching_dp()
    print(f"Video Stitching Greedy Interval DP 100 iterations took {t*1000:.3f}ms")

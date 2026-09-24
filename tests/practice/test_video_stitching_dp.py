"""
Unit tests for Video Stitching Greedy Interval DP
"""
from algorithms.practice.dynamic_programming_1d.video_stitching_dp import solve_video_stitching_dp

def test_video_stitching_dp_base():
    assert solve_video_stitching_dp() is True
    assert solve_video_stitching_dp([3, 1, 2]) == [1, 2, 3]

def test_video_stitching_dp_edge_cases():
    assert solve_video_stitching_dp("") == ""
    assert solve_video_stitching_dp(0) is True
    assert solve_video_stitching_dp(-5) is False

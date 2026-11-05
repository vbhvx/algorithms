"""
Unit tests for Video Stitching Maximum Forward Reach
"""
from algorithms.practice.intervals_scheduling.video_stitching_greedy import solve_video_stitching_greedy

def test_video_stitching_greedy_base():
    assert solve_video_stitching_greedy() is True
    assert solve_video_stitching_greedy([3, 1, 2]) == [1, 2, 3]

def test_video_stitching_greedy_edge_cases():
    assert solve_video_stitching_greedy("") == ""
    assert solve_video_stitching_greedy(0) is True
    assert solve_video_stitching_greedy(-5) is False

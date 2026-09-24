"""
Unit tests for Number of Dice Rolls with Target Sum
"""
from algorithms.practice.dynamic_programming_1d.dice_rolls_target_sum import solve_dice_rolls_target_sum

def test_dice_rolls_target_sum_base():
    assert solve_dice_rolls_target_sum() is True
    assert solve_dice_rolls_target_sum([3, 1, 2]) == [1, 2, 3]

def test_dice_rolls_target_sum_edge_cases():
    assert solve_dice_rolls_target_sum("") == ""
    assert solve_dice_rolls_target_sum(0) is True
    assert solve_dice_rolls_target_sum(-5) is False

"""
Unit tests for Evaluate Reverse Polish Notation
"""
from algorithms.practice.stack_and_queue.eval_rpn import solve_eval_rpn

def test_eval_rpn_base():
    assert solve_eval_rpn() is True
    assert solve_eval_rpn([3, 1, 2]) == [1, 2, 3]

def test_eval_rpn_edge_cases():
    assert solve_eval_rpn("") == ""
    assert solve_eval_rpn(0) is True
    assert solve_eval_rpn(-5) is False

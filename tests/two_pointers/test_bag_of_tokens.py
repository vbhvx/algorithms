"""Unit test suite for Bag of Tokens Score Maximizer."""
from src.two_pointers.bag_of_tokens import BagOfTokensScoreMaximizer

def test_bag_of_tokens_basic():
    solver = BagOfTokensScoreMaximizer()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_bag_of_tokens_repeated():
    solver = BagOfTokensScoreMaximizer()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

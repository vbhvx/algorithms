"""Unit test suite for Product of Array Except Self."""
from src.arrays_and_hashing.product_except_self import ProductOfArrayExceptSelf

def test_product_except_self_basic():
    solver = ProductOfArrayExceptSelf()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_product_except_self_repeated():
    solver = ProductOfArrayExceptSelf()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

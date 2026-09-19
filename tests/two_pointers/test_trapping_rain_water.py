"""Unit test suite for Trapping Rain Water Max Bounds."""
from src.two_pointers.trapping_rain_water import TrappingRainWaterMaxBounds

def test_trapping_rain_water_basic():
    solver = TrappingRainWaterMaxBounds()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_trapping_rain_water_repeated():
    solver = TrappingRainWaterMaxBounds()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

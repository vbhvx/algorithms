"""Unit test suite for Encode Decode Strings Framing."""
from src.arrays_and_hashing.encode_decode_strings import EncodeDecodeStringsFraming

def test_encode_decode_strings_basic():
    solver = EncodeDecodeStringsFraming()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_encode_decode_strings_repeated():
    solver = EncodeDecodeStringsFraming()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5

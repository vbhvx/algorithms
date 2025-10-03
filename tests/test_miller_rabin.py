from algorithms.math_geometry.miller_rabin import is_prime_miller_rabin

def test_miller_rabin():
    assert is_prime_miller_rabin(1000000007)
    assert not is_prime_miller_rabin(1000000005)

from algorithms.math_geometry.gcd import extended_gcd, mod_inverse

def test_gcd():
    gcd, x, y = extended_gcd(30, 20)
    assert gcd == 10
    assert mod_inverse(3, 11) == 4

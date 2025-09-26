"""Extended Euclidean algorithm for GCD and modular multiplicative inverse."""

def extended_gcd(a: int, b: int):
    if a == 0: return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1; y = x1
    return gcd, x, y

def mod_inverse(a: int, m: int) -> int:
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1: raise ValueError("Inverse doesn't exist")
    return (x % m + m) % m

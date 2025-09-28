"""Miller-Rabin probabilistic primality test."""

def is_prime_miller_rabin(n: int, k: int = 5) -> bool:
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    d = n - 1; s = 0
    while d % 2 == 0: d //= 2; s += 1
    for a in [2, 3, 5, 7, 11][:k]:
        if n <= a: break
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

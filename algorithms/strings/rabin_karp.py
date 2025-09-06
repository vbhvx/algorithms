"""Rabin-Karp algorithm with polynomial rolling hash."""
from typing import List

PRIME = 101; BASE = 256

def rabin_karp_search(text: str, pattern: str) -> List[int]:
    n, m = len(text), len(pattern)
    if m > n or m == 0: return []
    p_hash = 0; t_hash = 0; h = 1
    for _ in range(m - 1): h = (h * BASE) % PRIME
    for i in range(m):
        p_hash = (BASE * p_hash + ord(pattern[i])) % PRIME
        t_hash = (BASE * t_hash + ord(text[i])) % PRIME
    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern: matches.append(i)
        if i < n - m:
            t_hash = (BASE * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % PRIME
            if t_hash < 0: t_hash += PRIME
    return matches

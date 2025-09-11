"""Manacher's linear time longest palindromic substring algorithm."""

def longest_palindrome_manacher(s: str) -> str:
    if not s: return ""
    t = "^#" + "#".join(s) + "#$"
    n = len(t); p = [0] * n; c = r = 0
    for i in range(1, n - 1):
        i_mirror = 2 * c - i
        if r > i: p[i] = min(r - i, p[i_mirror])
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]: p[i] += 1
        if i + p[i] > r: c = i; r = i + p[i]
    max_len, center_idx = max((val, idx) for idx, val in enumerate(p))
    start = (center_idx - max_len) // 2
    return s[start:start + max_len]

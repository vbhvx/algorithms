from algorithms.strings.kmp import kmp_search, compute_lps

def test_kmp():
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AAAAABAAABA", "AAAA") == [0, 1]

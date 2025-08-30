from algorithms.dp.lcs import longest_common_subsequence

def test_lcs():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "def") == 0

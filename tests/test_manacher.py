from algorithms.strings.manacher import longest_palindrome_manacher

def test_manacher():
    assert longest_palindrome_manacher("babad") in ["bab", "aba"]
    assert longest_palindrome_manacher("cbbd") == "bb"

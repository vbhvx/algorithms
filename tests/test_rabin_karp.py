from algorithms.strings.rabin_karp import rabin_karp_search

def test_rabin_karp():
    assert rabin_karp_search("GEEKS FOR GEEKS", "GEEK") == [0, 10]

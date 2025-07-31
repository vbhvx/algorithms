from algorithms.searching.binary_search import binary_search

def test_binary_search():
    arr = [2, 3, 4, 10, 40]
    assert binary_search(arr, 10) == 3
    assert binary_search(arr, -1) == -1

from algorithms.backtracking.combinations import permutations

def test_permutations():
    assert len(permutations([1, 2, 3])) == 6

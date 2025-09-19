from algorithms.backtracking.n_queens import solve_n_queens

def test_n_queens():
    assert len(solve_n_queens(4)) == 2
    assert len(solve_n_queens(1)) == 1

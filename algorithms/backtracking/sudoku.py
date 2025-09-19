"""9x9 Sudoku solver using backtracking with row/col/box validity checks."""

def solve_sudoku(board) -> bool:
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch: return False
            if board[i][c] == ch: return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch: return False
        return True
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for d in "123456789":
                    if is_valid(r, c, d):
                        board[r][c] = d
                        if solve_sudoku(board): return True
                        board[r][c] = "."
                return False
    return True

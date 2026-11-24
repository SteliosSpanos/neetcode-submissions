class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def capture_safe_region(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O"):
                return

            board[r][c] = "T"
            for dr, dc in directions:
                capture_safe_region(r+dr, c+dc)

        for r in range(ROWS):
            capture_safe_region(r, 0)
            capture_safe_region(r, COLS - 1)
        for c in range(COLS):
            capture_safe_region(0, c)
            capture_safe_region(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
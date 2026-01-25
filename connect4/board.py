EMPTY = 0
RED = 1
YELLOW = -1

class Board:
    def __init__(self):
        self.grid = [[EMPTY] * 7 for i in range(6)]

    def moves(self):
        return [col for col in range(7) if self.grid[0][col] == EMPTY] #for empty cells top of cols

    def drop_piece(self, col, player):
        for p in range(5, -1, -1):
            if self.grid[p][col] == EMPTY:
                self.grid[p][col] = player
                return

    def undo_piece(self, col):
        for r in range(6):
            if self.grid[r][col] != EMPTY:
                self.grid[r][col] = EMPTY
                return

    def is_full(self):
        return all(self.grid[0][c] != EMPTY for c in range(7))

    def is_draw(self):
        return self.is_full() and self.check_winner() == EMPTY

    def check_winner(self):
        grid = self.grid

        for r in range(6):
            for c in range(4):
                p = grid[r][c]
                if p != EMPTY and p == grid[r][c+1] == grid[r][c+2] == grid[r][c+3]:
                    return p #return horizontal check

        for r in range(3):
            for c in range(7):
                p = grid[r][c]
                if p != EMPTY and p == grid[r+1][c] == grid[r+2][c] == grid[r+3][c]:
                    return p #return vertical check

        for r in range(3):
            for c in range(4):
                p = grid[r][c]
                if p != EMPTY and p == grid[r+1][c+1] == grid[r+2][c+2] == grid[r+3][c+3]:
                    return p #return diagonal downright check

        for r in range(3, 6):
            for c in range(4):
                p = grid[r][c]
                if p != EMPTY and p == grid[r-1][c+1] == grid[r-2][c+2] == grid[r-3][c+3]:
                    return p #return diagonal upright check

        return EMPTY

    def to_ascii(self):
        lines = []
        for r in range(6):
            row = []
            for c in range(7):
                rep = self.grid[r][c]
                if rep == EMPTY:
                    row.append(".")
                elif rep == RED:
                    row.append("R")
                else:
                    row.append("Y")
            lines.append(" ".join(row))
        lines.append("0 1 2 3 4 5 6")
        return "\n".join(lines)


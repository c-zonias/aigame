EMPTY = 0
RED = 1
YELLOW = -1

class Board:
    def __init__(self):
        self.grid = [[EMPTY] * 7 for i in range(6)]


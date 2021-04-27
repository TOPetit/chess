from enum import Enum
from typing import List, Optional, Tuple


class Pieces(Enum):
    PAWN = "p"
    BISHOP = "b"
    ROOK = "r"
    KNIGHT = "n"
    QUEEN = "q"
    KING = "k"


class Colors(Enum):
    WHITE = 1
    BLACK = 2


class Board:
    def __init__(self) -> None:
        self.board: List[List[Optional[Tuple[Pieces, Colors]]]] = [
            [None] * 8 for i in range(8)
        ]

    def reset(self) -> None:
        for color, row in ((Colors.WHITE, 0), (Colors.BLACK, 7)):
            self.board[row][0] = self.board[row][7] = (Pieces.ROOK, color)
            self.board[row][1] = self.board[row][6] = (Pieces.KNIGHT, color)
            self.board[row][2] = self.board[row][5] = (Pieces.BISHOP, color)
            self.board[row][3] = (Pieces.KING, color)
            self.board[row][4] = (Pieces.QUEEN, color)
            row = {0: 1, 7: 6}[row]
            for i in range(8):
                self.board[row][i] = (Pieces.PAWN, color)

    def print(self) -> None:
        for row in range(7, -1, -1):
            for file in range(8):
                cell = self.board[row][file]
                if cell is None:
                    print(" ", end="")
                    continue
                piece, color = cell
                char: str = piece.value
                if color == Colors.WHITE:
                    char = char.upper()
                print(char, end="")
            print()


if __name__ == "__main__":
    b = Board()
    b.reset()
    b.print()

from os import PathLike
from typing import Union


class FastScanner:
    def __init__(self, file: Union[PathLike, int] = 0):
        self.fd = open(file, "r", encoding="utf-8")
        self.tokens = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.fd.close()

    def next(self):
        while not self.tokens:
            self.tokens = self.fd.readline().split()

        return self.tokens.pop(0)

    def __str__(self):
        return self.next()

    def __int__(self):
        return int(self.next())


class PrintWriter:
    def __init__(self, file: Union[PathLike, int] = 1):
        self.fd = open(file, "w", encoding="utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.fd.close()

    def write(self, obj):
        self.fd.write(str(obj))

    def writeln(self, obj):
        self.write(obj)
        self.fd.write("\n")


def solve():
    with FastScanner() as in_, PrintWriter() as out_:
        n = int(in_)
        m = int(in_)

        board = [[int(in_) for _ in range(m)] for _ in range(n)]
        maximum = board[0][0]

        for i in range(1, n):
            for j in range(1, m):
                if board[i][j] != 0:
                    a = board[i][j - 1]
                    b = board[i - 1][j]
                    c = board[i - 1][j - 1]

                    board[i][j] = min(a, b, c) + 1
                    maximum = max(maximum, board[i][j])

        out_.writeln(maximum)


if __name__ == "__main__":
    solve()

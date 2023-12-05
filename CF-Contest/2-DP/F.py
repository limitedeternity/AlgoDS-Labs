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

        board = [[0 for _ in range(2 * m)] for _ in range(2 * n)]
        board[n][m] = 1

        for i in range(n, 2 * n):
            for j in range(m, 2 * m):
                if i != n and j != m:
                    board[i][j] = board[i - 2][j - 1] + board[i - 1][j - 2]

        out_.writeln(board[2 * n - 1][2 * m - 1])


if __name__ == "__main__":
    solve()

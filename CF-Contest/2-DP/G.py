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
    MOD = 10 ** 6 + 7
    with FastScanner() as in_, PrintWriter() as out_:
        n = int(in_)
        m = int(in_)
        
        board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        board[0][0] = 1

        for j in range(m):
            i = 0
            q = j

            while i < n and q >= 0:
                if i + 2 <= n and q + 1 <= m:
                    board[i + 2][q + 1] = (board[i + 2][q + 1] + board[i][q]) % MOD

                if i + 1 <= n and q + 2 <= m:
                    board[i + 1][q + 2] = (board[i + 1][q + 2] + board[i][q]) % MOD

                if i + 2 <= n and q - 1 >= 0:
                    board[i + 2][q - 1] = (board[i + 2][q - 1] + board[i][q]) % MOD

                if i - 1 >= 0 and q + 2 <= m:
                    board[i - 1][q + 2] = (board[i - 1][q + 2] + board[i][q]) % MOD

                i += 1
                q -= 1

        for i in range(1, n):
            q = i
            j = m - 1

            while q < n and j >= 0:
                if q + 2 <= n and j + 1 <= m:
                    board[q + 2][j + 1] = (board[q + 2][j + 1] + board[q][j]) % MOD

                if q + 1 <= n and j + 2 <= m:
                    board[q + 1][j + 2] = (board[q + 1][j + 2] + board[q][j]) % MOD

                if q + 2 <= n and j - 1 >= 0:
                    board[q + 2][j - 1] = (board[q + 2][j - 1] + board[q][j]) % MOD

                if q - 1 >= 0 and j + 2 <= m:
                    board[q - 1][j + 2] = (board[q - 1][j + 2] + board[q][j]) % MOD

                q += 1
                j -= 1

        out_.writeln(board[n - 1][m - 1] % MOD)


if __name__ == "__main__":
    solve()

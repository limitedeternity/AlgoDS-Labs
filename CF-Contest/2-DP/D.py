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
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = board[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + board[i][0]

        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + board[0][i]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = board[i][j] + max(dp[i][j - 1], dp[i - 1][j])

        i, j = n - 1, m - 1
        path = []

        while i != 0 or j != 0:
            if i != 0:
                if dp[i - 1][j] == dp[i][j] - board[i][j]:
                    i -= 1
                    path.append("D")

                else:
                    if j != 0:
                        j -= 1
                        path.append("R")

                    else:
                        path.append("D")

            else:
                j -= 1
                path.append("R")

        path_answer = "".join(path[::-1])

        out_.writeln(dp[n - 1][m - 1])
        out_.writeln(path_answer)
        

if __name__ == "__main__":
    solve()

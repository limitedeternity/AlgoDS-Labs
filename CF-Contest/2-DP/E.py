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
    MOD = 10 ** 9 + 7
    with FastScanner() as in_, PrintWriter() as out_:
        k = int(in_)
        s = int(in_)

        dp = [[0 for _ in range(s + 1)] for _ in range(k + 1)]
        dp[0][0] = 1

        for i in range(k + 1):
            for j in range(s + 1):
                for m in range(10):
                    if j >= m:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - m]) % MOD

        out_.writeln(dp[k][s])


if __name__ == "__main__":
    solve()

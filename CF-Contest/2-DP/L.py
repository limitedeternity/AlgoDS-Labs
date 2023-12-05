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
        a = int(in_)
        k = int(in_)
        b = int(in_)
        m = int(in_)

        seq, dp = [0] * n, [float("inf")] * (n + 1)
        seq[0] = a
        dp[0] = float("-inf")

        for i in range(1, n):
            seq[i] = (k * seq[i - 1] + b) % m

        answer = float("-inf")
        for i in range(n):
            l, r = 0, n

            while l < r - 1:
                m = (l + r) // 2

                if dp[m] >= seq[i]:
                    r = m

                else:
                    l = m

            if dp[r - 1] < seq[i] and seq[i] < dp[r]:
                dp[r] = seq[i]
                answer = max(answer, r)

        out_.writeln(answer)


if __name__ == "__main__":
    solve()

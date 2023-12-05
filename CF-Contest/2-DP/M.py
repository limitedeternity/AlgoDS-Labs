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
        s = int(in_)
        w = sorted([int(in_) for _ in range(n)])

        backpack = [[0 for _ in range(10001)] for _ in range(n + 1)]
        loop = True

        for i in range(n):
            if loop:
                for j in range(s + 1):
                    if i > 0:
                        backpack[i][j] = backpack[i - 1][j]

                    if j >= w[i]:
                        if i > 0:
                            backpack[i][j] = max(backpack[i][j], backpack[i - 1][j - w[i]] + w[i])

                        else:
                            backpack[i][j] = w[i]

            else:
                break

        out_.writeln("YES" if backpack[n - 1][s] == s else "NO")


if __name__ == "__main__":
    solve()

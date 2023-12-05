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


def levenshtein(lhs, rhs):
    distances = [[0 for _ in range(len(rhs) + 1)] for _ in range(len(lhs) + 1)]

    for t in range(len(lhs) + 1):
        distances[t][0] = t

    for t in range(len(rhs) + 1):
        distances[0][t] = t

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(lhs) + 1):
        for t2 in range(1, len(rhs) + 1):
            if lhs[t1 - 1] == rhs[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]

            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                distances[t1][t2] = min(a, b, c) + 1

    return distances[len(lhs)][len(rhs)]


def solve():
    with FastScanner() as in_, PrintWriter() as out_:
        lhs = str(in_)
        rhs = str(in_)
        out_.writeln(levenshtein(lhs, rhs))


if __name__ == "__main__":
    solve()

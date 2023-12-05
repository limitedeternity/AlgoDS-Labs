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
        arr = [int(in_) for _ in range(n)]

        lis = [1] * n
        prev = list(range(n))

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    prev[i] = j

        idx, maximum = max(enumerate(lis), key=lambda v: v[1])
        seq = [arr[idx]]

        while idx != prev[idx]:
            idx = prev[idx]
            seq.append(arr[idx])

        out_.writeln(maximum)
        out_.writeln(" ".join(str(x) for x in seq[::-1]))


if __name__ == "__main__":
    solve()

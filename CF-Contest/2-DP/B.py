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
        k = int(in_)

        arr = [0] * (n + 1)
        for i in range(2, n):
            arr[i] = int(in_)

        stairs, indexes = [0] * (n + 1), [0] * (n + 1)  
        path = []

        for i in range(2, n + 1):
            local, index = float("-inf"), -1
            counter, j = 0, i - 1

            while counter < k and j > 0:
                if stairs[j] > local:
                    local = stairs[j]
                    index = j

                counter += 1
                j -= 1

            indexes[i] = index
            stairs[i] = arr[i] + local

        current, count = n, 0
        path.append(current)

        while current > 1:
            count += 1
            current = indexes[current]
            path.append(current)

        path_answer = " ".join(map(str, path[::-1]))

        out_.writeln(stairs[n])
        out_.writeln(count)
        out_.writeln(path_answer)


if __name__ == "__main__":
    solve()

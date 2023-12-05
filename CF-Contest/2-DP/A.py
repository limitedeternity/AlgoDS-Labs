import sys
from itertools import islice

input = sys.stdin.readline
print = sys.stdout.write


def fibs():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

def fib(n):
    return next(islice(fibs(), n, None))


if __name__ == "__main__":
    N = int(input())
    print(str(fib(N)))

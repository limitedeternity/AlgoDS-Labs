import random
import sys

input = sys.stdin.readline
print = sys.stdout.write


def algo(n, s):
    if n <= 0:
        print("NO\n")
        return

    seen = set()

    if s != 0:
        if n % 2 == 0:
            seen.add(s)
            seen.add(0)
            n -= 2

        else:
            seen.add(s)
            n -= 1

    else:
        if n % 2 == 0:
            seen.add(-5)
            seen.add(5)
            n -= 2

        else:
            seen.add(s)
            n -= 1

    while n > 0:
        rand = random.randrange(-(10**9), 10**9)

        if rand not in seen:
            seen.add(rand)
            seen.add(-rand)
            n -= 2

    print("YES\n")
    print(" ".join(map(str, seen)))
    print("\n")


algo(int(input()), int(input()))

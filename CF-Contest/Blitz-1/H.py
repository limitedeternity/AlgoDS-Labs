from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))

    if n <= 1:
        print(" ".join(map(str, perm)))
        print("\n")
        continue

    result = deque()
    result.append(perm[0])

    for i in range(1, n):
        if perm[i] < result[0]:
            result.appendleft(perm[i])

        else:
            result.append(perm[i])

    print(" ".join(map(str, result)))
    print("\n")

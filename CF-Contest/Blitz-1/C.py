from math import sqrt
import sys

input = sys.stdin.readline
print = sys.stdout.write


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


n, m = map(int, input().split())
x, y, r = map(int, input().split())

result = 0
for x1 in range(n):
    for y1 in range(m):
        if distance(x1, y1, x, y) <= r:
            result += 1

print(str(result))

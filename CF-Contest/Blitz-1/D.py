from collections import OrderedDict
import sys

input = sys.stdin.readline
print = sys.stdout.write

n, t = map(int, input().split())
xchg = list(map(int, input().split()))

result = OrderedDict.fromkeys(range(1, n + 1))
for i in xchg:
    result.move_to_end(i)

print(" ".join(map(str, result.keys())))

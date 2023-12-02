import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))
a.sort()

result = a[n - 1] * n
s = sum(a)
m = max(a)

for i in range(n):
    cur = a[i] * (i + 1) + m * (n - 1 - i) - s
    result = min(result, cur)

print(str(result))

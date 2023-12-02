import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
l, r = float("-inf"), float("inf")

for _ in range(n):
    cmd, num = map(int, input().split())

    if cmd == 1:
        if num >= r:
            l = r = num

        elif num >= l:
            l = num

    elif cmd == 2:
        if num <= l:
            l = r = num

        elif num <= r:
            r = num

    elif cmd == 3:
        if num <= l:
            print(str(l))
            print("\n")

        elif num >= r:
            print(str(r))
            print("\n")

        else:
            print(str(num))
            print("\n")

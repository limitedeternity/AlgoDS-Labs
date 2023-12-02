import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

m = int(input())

vacant = [x for x in range(1, m + 1)]
heapq.heapify(vacant)

occupied = {}

for _ in range(m):
    cmd, car = input().split()

    if cmd == "+":
        occupied[car] = heapq.heappop(vacant)

        print(str(occupied[car]))
        print("\n")

    elif cmd == "-":
        heapq.heappush(vacant, occupied[car])
        del occupied[car]


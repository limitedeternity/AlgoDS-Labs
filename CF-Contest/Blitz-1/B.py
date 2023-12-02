import sys

input = sys.stdin.readline
print = sys.stdout.write


def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))

def palindrome_split(s):
    half, rem = divmod(len(s), 2)
    return iter(s[:half]), reversed(s[half + rem:])


n = int(input())
s = input()

cur_max = 0

for l in range(n):
    for r in range(l, n):
        substr = s[l : r + 1]
        error_cnt = hamming_distance(*palindrome_split(substr))

        if error_cnt <= 1:
            cur_max = max(cur_max, r - l + 1)

print(str(cur_max))

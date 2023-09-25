from collections import deque


def longest_balanced(string):
    brackets = { "{": "}", "(": ")", "[": "]" }
    stack = deque()

    cur_length = max_length = 0

    for char in string:
        if char in brackets:
            stack.append(char)
            cur_length += 1

        else:
            if len(stack) == 0 or brackets[stack.pop()] != char:
                cur_length = 0
                continue
                
        if len(stack) == 0:
            max_length = max(max_length, cur_length * 2)

    return max_length


assert(longest_balanced("))([]({})))(())") == 8)
assert(longest_balanced(")(([]({})))([]") == 10)
assert(longest_balanced("()(())((()") == 6)
assert(longest_balanced(")(([](})))[]") == 2)

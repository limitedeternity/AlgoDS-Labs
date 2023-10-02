from collections import deque


def longest_valid(string):
    brackets = { "{": "}", "(": ")", "[": "]" }
    stack = deque()
    stack.append((None, -1))

    max_length = 0

    for i, char in enumerate(string):
        if char in brackets:
            stack.append((char, i))

        else:
            open_br, _ = stack.pop()

            if brackets.get(open_br, open_br) != char:
                stack.append((None, i))
                continue

            _, last_i = stack[-1]
            max_length = max(max_length, i - last_i)

    return max_length


assert(longest_valid("))([]({})))(())") == 8)
assert(longest_valid(")(([]({})))([]") == 10)
assert(longest_valid("()(())((()") == 6)
assert(longest_valid(")(([](})))[]") == 2)
assert(longest_valid("(}[]") == 2)

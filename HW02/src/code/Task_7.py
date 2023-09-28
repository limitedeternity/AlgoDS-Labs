from collections import deque
from itertools import islice


def window_gen(sequence, size):
    assert(size > 0)

    iterator = iter(sequence)
    window = deque(islice(iterator, size), maxlen=size)

    yield window

    for elem in iterator:
        window.append(elem)
        yield window

def max_window_sum(sequence, k):
    return max(map(sum, window_gen(sequence, k)))

def max_sub_sum(sequence, l, r):
    return max(max_window_sum(sequence, k) for k in range(l, r + 1))


assert(max_sub_sum([1, 2, -5, 3, 2, -1, 5, -10, 3, 2], 2, 4) == 9)
assert(max_sub_sum([-1, -2, -5, -3, 10], 2, 5) == 7)

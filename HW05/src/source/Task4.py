import functools


def compare_strings(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def find_max_number_order(*strings):
    sorted_strings = sorted(
        strings, key=functools.cmp_to_key(compare_strings)
    )
    return ''.join(sorted_strings)

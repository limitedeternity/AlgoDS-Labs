def max_sub_sum(*sequence):
    current_sum = best_sum = 0

    for x in sequence:
        current_sum = max(0, x + current_sum)
        best_sum = max(current_sum, best_sum)

    return best_sum


assert(max_sub_sum(1, 2, -5, 3, 2, -1, 5, -10, 3, 2) == 9)
assert(max_sub_sum(-2, 1, -3, 4, -1, 2, 1, -5, 4) == 6)

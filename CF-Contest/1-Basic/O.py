def check(mid, array, k):
    count = 0
    current_sum = 0

    for el in array:
        if current_sum + el > mid:
            count += 1
            current_sum = el

        else:
            current_sum += el

    count += 1
    return count <= k

def min_max_sum(n, k, array):
    left = max(array)
    right = sum(array)

    while left < right:
        mid = left + (right - left) // 2

        if check(mid, array, k):
            right = mid

        else:
            left = mid + 1

    return left


[n, k] = list(map(int, input().split()))
array = list(map(int, input().split()))

print(min_max_sum(n, k, array))

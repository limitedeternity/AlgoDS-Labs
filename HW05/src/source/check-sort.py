def binary_search(a, key, left, right):
    if left == right - 1:
        return left
    else:
        mid = left + (right - left) / 2
        if key < a[mid]:
            return binary_search(a, key, left, mid)
        else:
            return binary_search(a, key, mid, right)
    

def check_sort(a):
    for r in range(0, k):
        i = random.range(0, n)
        j = binary_search(a, a[i], 0, len( a ))
        if i != j:
            return False
    return True

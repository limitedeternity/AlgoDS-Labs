def smallest_missing(arr):
    n = len(arr)

    for i in range(n):
        while (arr[i] >= 1
            and arr[i] <= n
            and arr[i] != arr[arr[i] - 1]):

            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
 
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
 
    return n + 1


def solve(arr, n):
    dp = [[0] * n for _ in range(n)]
    S = 0

    for i in range(n - 1, -1, -1):
        S += arr[i]

        for j in range(i, n):
            if i == j:
                dp[i][j] = arr[i]

            else:
                dp[i][j] = max(arr[i] - dp[i + 1][j], arr[j] - dp[i][j - 1])

    V = dp[0][n - 1]
    return (S + V) / 2


arr = [1, 2, 1000, 5]
print(solve(arr, len(arr))) # -> 1001

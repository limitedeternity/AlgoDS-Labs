def query_sum(source, queries):
    n = len(source)
    result = [0] * n

    for x, l, r in queries:
        result[l] += x
        if r + 1 < n:
            result[r + 1] -= x

    delta = 0

    for i in range(0, n):
        delta += result[i]
        result[i] = source[i] + delta
        yield result[i]


source = list(range(1, 11))
queries = [(2, 1, 3)]

for result in query_sum(source, queries):
    print(result)


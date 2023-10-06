import heapq
from itertools import product


def merge_sorted(a, b):
    return heapq.merge(
        *[
            map(sum, product([ai], b))
            for ai in a
        ]
    )


n = 5
a = range(n)
b = range(n, n * 2)

# \dotfill
# Сложность product(lst1, lst2): $O(|lst_1| \cdot |lst_2|)$
# \dotfill
# Сложность product([ai], b): $O(1 \cdot |b|) = O(n)$
# \dotfill
# Сложность sum(fst, snd): $O(1)$
# \dotfill
# Сложность map(sum, product([ai], b)): $O(1 \cdot n) = O(n)$
# \dotfill
# Сложность map(sum, product([ai], b)) for ai in a: $O(|a| \cdot n) = O(n^2)$ 
# \dotfill
# Сложность heapq.merge(*[...]): $O(n^2 \cdot log(|[...]|)) = O(n^2 \cdot log(n))$
# \dotfill

# Итоговая сложность алгоритма: $O(n^2 \cdot log(n))$
print(
    list(
        merge_sorted(a, b)
    )
)

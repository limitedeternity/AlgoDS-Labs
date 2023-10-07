import heapq


def second_largest(nums):
    # Построение: $O(n)$
    heapq._heapify_max(nums)
    
    # Удаление корня: $O(log(n))$
    heapq._heappop_max(nums)

    # Запрос корня: $O(1)$
    return nums[0]


lst = [3, 1, 11, 10]

# Итоговая сложность алгоритма: $O(n + log(n))$
print(second_largest(lst))


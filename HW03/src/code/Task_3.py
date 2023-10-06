import random

# Количество стойл
m = 6

# Количество коров
n = 3

# Координаты
coords = [2, 5, 7, 11, 15, 20]
random.shuffle(coords)


# Сложность solve: $O(m)$
def solve(sorted_coords, cow_count, distance):
    # Сразу занимаем крайнее левое стойло
    occupied_count = 1
    last_occupied = sorted_coords[0]

    for coord in sorted_coords:
        # Пропускаем те, что слишком близко к занятому
        if last_occupied + distance > coord:
            continue

        # Занимаем стойло
        occupied_count += 1
        last_occupied = coord

    # Все коровы должны поместиться
    return occupied_count >= cow_count


# Сложность сортировки (timsort): $O(m \cdot log(m))$
coords.sort()

# Границы (левая: $0$, правая: $x_{max}$)
left, right = 0, coords[-1]

# Найденная дистанция будет здесь
mid = -1

# Сложность бинарного поиска: $O(log(right - left)) = O(log(x_{max}))$
# Сложность solve: $O(m)$
# Комбинированная сложность: $O(m \cdot log(x_{max}))$
while left <= right:
    mid = (right + left) // 2

    if solve(coords, n, mid):
        left = mid + 1
    
    else:
        right = mid - 1

# Итоговая сложность алгоритма:
# $O(m \cdot log(m) + m \cdot log(x_{max})) = O(m \cdot (log(m) + log(x_{max})))$
print(mid)

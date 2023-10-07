import heapq


def merge_lists(*lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    result = []

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            heapq.heappush(heap, next_tuple)

    return result


assert(merge_lists([1, 4, 5], [1, 3, 4], [2, 6]) == [1, 1, 2, 3, 4, 4, 5, 6])


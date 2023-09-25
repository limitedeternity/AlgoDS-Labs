from collections import deque


def max_sub_sum(sequence, l, r):
    assert(r - l >= 0)
    assert(len(sequence) - l >= 0)

    current_sum = best_sum = 0
    current_window = deque()

    for x in sequence:
        if len(current_window) == r:
            elem = current_window.popleft()
            current_sum -= elem
            best_sum = max(current_sum, best_sum)
 
            temp_window = deque()
            print(current_window, current_sum, best_sum)

            while len(current_window) > l:
                elem = current_window.pop()
                current_sum -= elem
                best_sum = max(current_sum, best_sum)
            
                temp_window.appendleft(elem)
                print(current_window, current_sum, best_sum)

            while len(temp_window) > 0:
                elem = temp_window.popleft()
                current_sum += elem
                best_sum = max(current_sum, best_sum)
                
                current_window.append(elem)
                print(current_window, current_sum, best_sum)
            
        current_window.append(x)
        current_sum += x

        if l <= len(current_window) <= r:
            best_sum = max(current_sum, best_sum)
        
        print(current_window, current_sum, best_sum)
        print()

    return best_sum

    
assert(max_sub_sum([1, 2, -5, 3, 2, -1, 5, -10, 3, 2], 2, 4) == 9)

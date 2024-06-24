# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    new_arr = []
    for elem in A:
        if elem >= 0:
            new_arr.append(elem)
    
    if len(new_arr) != 0:
        min_edge = min(new_arr)
        max_edge = max(new_arr)

        range_arr = [new_digit for new_digit in range(min_edge,max_edge)]
        for digit_no in range_arr:
            if digit_no not in new_arr:
                return digit_no
        
        return max_edge + 1

    return 1



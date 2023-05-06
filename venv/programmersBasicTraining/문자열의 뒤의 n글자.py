def solution(my_string, n):
    slice_point = len(my_string) - n
    return my_string[slice_point:]
def solution(my_string, s, e):
    my_string_1 = my_string[:s-1]
    my_string_2 = my_string[e:]
    my_string_3 = my_string[s:e]
    my_string_3 = my_string_3[::-1]
    return my_string_1 + my_string_3 + my_string_2
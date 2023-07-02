def solution(my_string, queries):
    for query in queries:
        start, end = query[0], query[1]
        substring = my_string[start:end+1]
        reversed_substring = substring[::-1]
        my_string = my_string[:start] + reversed_substring + my_string[end+1:]
    return my_string


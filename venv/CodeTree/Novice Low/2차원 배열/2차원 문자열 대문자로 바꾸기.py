for i in range(5):
    alp = list(map(str, input().split()))
    answer = ' '.join([word.upper() for word in alp])
    print(answer)

# join()

# separator_string.join(iterable)

my_list = ['hello', 'world', '!']
result = ' '.join(my_list)
print(result)

result = ''.join(my_list)
print(result)

my_string = 'python'
result = '.'.join(my_string)
print(result)

result = ','.join(my_string)
print(result)
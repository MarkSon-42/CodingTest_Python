# LOOP

sum_int_01 = 0
for i in range(1, 10 + 1):
    sum_int_01 += i

sum_int_02 = sum(i for i in range(1, 10 + 1))

sum_int_03 = sum(range(1, 10 + 1))

print(sum_int_01)
print(sum_int_02)
print(sum_int_03)

# List Comprehension : 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

list_map_lambda = list(map(lambda x: x + 10, [1, 2, 3]))

print(list_map_lambda)

#

list_comp = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(list_comp)

# same as above

a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)
print(a)

# range

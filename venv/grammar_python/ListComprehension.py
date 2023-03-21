# https://www.geeksforgeeks.org/python-list-comprehension/

# newList = [expression(element) for element in oldList if condition]

# Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.

List = [character for character in [1, 2, 3]]

print(List)

list = [i for i in range(11) if i % 2 == 0]
print(list)

matrix = [[j for j in range(5)] for j in range(5)]
print(matrix)

List = []

for character in 'Geeks 4 Geeks!':
    List.append(character)

print(List)




# Time Analysis in List Comprehensions and Loop
import time

def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result



def list_comprehension(n):
    return [i**2 for i in range(n)]


# Driver Code

# Calculate time taken by for_loop()
begin = time.time()
for_loop(10 ** 6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for_loop:', round(end - begin, 2))

# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10 ** 6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end - begin, 2))




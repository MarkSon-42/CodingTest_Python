

n = int(input()) # read a single integer
arr = list(map(int, input().split())) # read a list of integers
s = input().strip() # read a string and strip leading/trailing whitespaces

name = 'Alice'
age = 25
print("My name is {0} and I am {1} years old.".format(name, age))

# {index} _ 중괄호에 파라미터 인덱스를 넣는 방식

# Reading input file

with open('input.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
    s = f.readline().strip()


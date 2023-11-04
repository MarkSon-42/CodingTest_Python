import sys

val = input("Enter your value: ")
print(val)
print(type(val)) # out : 123 <class 'str'>

string = str(input())
print(string)

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print(x, y)


a, b, c, d = input("Enter four numbers").split()
print(a, b, c, d)


# using List comprehension

g, h, j = [int(x) for x in input("Enter two values: ").split()]
print(g, h, j)

def get_ints(): return map(int, sys.stdin.readline().strip().split())

v, b, n, m = get_ints()


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


Arr = get_ints()
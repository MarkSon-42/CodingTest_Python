# 람다 함수

# 람다식

# 익명 함수

# Annonymous Functions

# def : with name ( normal function )

# lambda : without name

# how to declare
# lambda arguments : expression

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))

string = 'GeeksforGeeks'

# lambda returns a function object
print(lambda string: string)

def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y


lambda_cube = lambda num: num ** 3

print(cube(6))

print("invoking lambda function..", lambda_cube(5))


# The lambda function gets more helpful when used inside a function.

# use lambda function inside map(), filter(), sorted() and many other functions

# sorted() with lambda
lst = ["1", "3", "8", "-1", "100", "91", "-26"]

print(sorted(lst, key=lambda x: int(x)))


# map() with lambda

# filter() with lambda
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(filter(lambda x: x % 2 != 0, my_list))
print(new_list)


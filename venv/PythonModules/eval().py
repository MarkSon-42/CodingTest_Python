x = 5
result = eval("x + 2")
print(result)


x = 10
eval("x + 3")
print(x) # output : 13

func_str = "def add(x, y):\n\treturn x + y"
eval(func_str)
result = add(2, 3)
print(result)
# wow... 이건 개쩐다...!


user_input = input("Enter a Python expression : ")
result = eval(user_input)
print(result)



numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair) # out : tuple로 엮어준다.

for i in range(3):
    pair = (numbers[i], letters[i])
    print(pair)

for number, upper, lower in zip("12345", "ABCDE", 'abcde'):
    print(number, upper, lower)

# 인자의 길이가 다를 때,

numbers = ["1", "2", "3"]
letters = ["A"]
list(zip(numbers, letters))

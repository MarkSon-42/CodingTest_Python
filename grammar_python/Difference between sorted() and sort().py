# sorted () : This method doesn’t effect the original sequence.
# sorted() -> 원래 리스트에는 영향 안준다. ( 정렬한 복사본을 반환한다 ), (파이썬 내장함수)
# sort() -> 원래 리스트를 정렬된 리스트로 바꿔버린다. ( 리스트 자료형의 메소드 )

# Python program to demonstrate
# sorted()


L = [5, 6, 8, 5, 9, 3, 6, 2, 9]


print("Sorted list:")
print(sorted(L))

print("\nReverse sorted list:")
print(sorted(L, reverse=True))

# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = 'python'
print(sorted(x))

# Dictionary : 키값을 아스키 순으로 정렬해서 키값을 리턴한다.
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))


L = ['aaaa', 'bbb', 'cc', 'd', 'jfdwifdi', 'dsq', 'dsuhigorkl']

print(sorted(L, key=len))


# Using key parameter

def sort_second(val):
    return val[1]


list1 = [(1, 2), (3, 3), (1, 1)]

list1.sort(key=sort_second)
print(list1)

list1.sort(key=sort_second, reverse = True)
print(list1)


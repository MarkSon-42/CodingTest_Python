# "파이썬 알고리즘 인터뷰 _ 박상길" 책을 공부하면서 실습, 정리한 내용임.

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

print(list(range(5)))

#       ->  [0, 1, 2, 3, 4]

print(range(5))

# range(0, 5)

print(type(range(5)))

# class 'range'

for i in range(5):
    print(i, end=' ')

print('\n')
# enumerate : '열거하다'는 뜻의 함수로, 여러 가지 자료형(list, set, tuple.. 등)을 인덱스를 포함한
# enumerate 객체로 리턴한다.

nums = [1, 2, 3, 2, 45, 2, 5]
eum = enumerate(nums)
print(eum) #

eum_list = list(enumerate(nums))
print(eum_list)

print("enumerate()는  인덱스를 포함한 객체를 만들어주는거야~")


# b = ['a1', 'b1', 'c1'] 가 있을 때 이 리스트의 인덱스와 값을 함께 출력하려면 ?
b = ['a1', 'b1', 'c1']
for i in range(len(b)):
    print(i, b[i])

# 위 코드는 값을 가져오기 위해 불필요한 b[i] 조회 작업과 전체 길이를 조회하여 루프를 처리하는 형태이다.
# 굳이 range()를 사용할 필요가 없다.

i = 0
for v in b:
    print(i, v)
    i += 1

# 위 보다는 깔끔하게 처리했으나, 이 경우 인덱스를 위한 변수를 별도로 관리하는 형태라 이 또한 좋은 코드는 아니다.

for i, v in enumerate(b):
    print(i, v)

# enumerate()를 통해 이상적으로 처리했다.




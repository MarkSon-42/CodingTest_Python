# "파이썬 알고리즘 인터뷰 _ 박상길" 책을 공부하면서 실습, 정리한 내용임.

# ------------나눗셈 연산자---------------------------

print(5 / 3)

t = type(5 / 3)
print(t)

t_int = type(5 // 3)
print(t_int)

# 나눗셈 연산자 // 는 int(a / b)와 동일하다

# 몫과 나머지를 동시에 구할 때 : divmod(5, 3)

print(divmod(21, 4))


# ---------- print()를 잘 써보자 --------------------


print('A1', 'B1')
# 출력시 공백이 디폴트로 추가된다.

print('A1', 'B1', sep=',')
# sep 옵션으로 , 을 추가해줄 수 있다!

print('aa', end=' ')
print('bb')
# print()는 디폴트로 줄바꿈도 하기 때문에, (end='\n' : default) 위처럼 공백을 옵셥으로 주면 줄바꿈 하지 않고 다음 프린트와 나란히 출력됨)

x = ['X', 'Y']
print(' '.join(x)) # 리스트를 출력할 떄는 join()으로 묶어서 처리한다.

idx = 1
fruit = "Apple"

# idx 값에 1을 더해서 fruit와 함께 출력하는 방법은?

print('{0}: {1}'.format(idx + 1, fruit)) # 1st way

print('{}: {}'.format(idx + 1, fruit)) # 2nd way

print(f'{idx + 1}: {fruit}') # wow...

# ----------------- pass -------------------------------

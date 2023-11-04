# for <원소> in <목록>:
for letter in ['A', 'B', 'C']:
    print(letter)

# general
i = 0
for letter in ['A', 'B', 'C']:
    print(i, letter)
    i += 1

# range()
# 0 부터 인자로 받은 것의 -1 까지 범위 설정!

ll = ['a', 'b', 'c', 'd']
for i in range(len(ll)):
    lett = ll[i]
    print(i, lett)


# enumerate()
# for <원소> in enumerate(<목록>):
# 튜플 형식으로 인덱스와 함께 출력해줌.
for entry in enumerate(['A', 'B', 'C']):
    print(entry)

# 인덱스와 원소를 각각 다른 변수에 할당하기 위해서는 unpacking(인자 풀기)을 해줘야함!
for i, alp in enumerate(['A', 'B', 'C']):
    print(i, alp)

# 인덱스를 0부터 말고 다른 시작점 설정하기.

for i, alp in enumerate(['A', 'B', 'C'], start=1):
    print(i, alp)


# enumerate()의 원리

iter_letters = iter(['A', 'B', 'C'])
print(next(iter_letters))
print(next(iter_letters))
print(next(iter_letters))

# python은 내부적으로 in 뒤에 오는 목록을 next()를 계속해서 호출함.


# list형태로 반환하기


# 2차원 리스트 루프

# general
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
for r in range(len(matrix)): # row index increase
    for c in range(len(matrix[r])): # column index increase
        print(r, c, matrix[r][c])

# enumerate() : 가독성 up, 실수가 줄어든다.
# 현업에서 위의 general처럼 작성하면 인덱스 값들 r, c 에 오타 발생 가능성
# 이를 방지하는 차원에서도 enumerate()가 좋다!
for r, row in enumerate(matrix):
    for c, letter in enumerate(row):
        print(r, c, letter)
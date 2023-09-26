arr = [1, 2, 3, 5]

new_arr = []
for elem in arr:
    new_arr.append(elem * 2)

print(new_arr)

#  for loop과 함께 append만 적용하는 경우
#  -> list comprehension 가능!

# list comprehension을 이용하면 선언과 동시에
# for loop으로 부터 나온 원소를 원하는 값으로 변경해줄 수 있음.
# [(append 안에 들어갈 내용) (for loop)]

arr_lc = [1, 2, 3, 5]
new_lc = [elem * 2 for elem in arr]
print(new_lc)

list_ = [i ** 2 for i in range(1, 10) if i % 2 == 1]
print(list_)

# 우리는 리스트에 i를 제곱한 결과를 저장할 거야
# i의 범위는 range(1, 10) 에서 뽑히는 숫자들이야
# 단, i를 2로 나눈 값이 1이 아니라면 리스트에 넣지 않을꺼야
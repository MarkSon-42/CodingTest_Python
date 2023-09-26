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

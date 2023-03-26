# Define the size of the table
size = 10

# nested loop : 중첩 반복문
for i in range(1, size + 1):
    for j in range(1, size + 1):
        product = i * j
        print(f"{i} x {j} = {product}")
        # f-string of python
        # ref : https://blockdmask.tistory.com/429


# Optimization

optm = 9

# 중첩 반복문을 하는데, 프린트를 계속 찍지 말고 빈 문자열에 한방에 넣어준다. (이건 손으로 써봐야 될 정도로 중요해)

for x in range(1, optm + 1):
    row = ""  # declare empty string : row
    for y in range(1, optm + 1):
        row += f"{x} x {y} = {x*y}\n"
    print(row)
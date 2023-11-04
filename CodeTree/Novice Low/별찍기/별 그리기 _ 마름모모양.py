# 요건 노트에 적어두라.. 반복문 개념 + 대칭

n = int(input())

# 위쪽 반쪽 다이아몬드 그리기
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 아래쪽 반쪽 다이아몬드 그리기
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

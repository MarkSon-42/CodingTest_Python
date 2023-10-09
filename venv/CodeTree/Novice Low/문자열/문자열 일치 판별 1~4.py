#    1

n, A = map(str, input().split())
n = int(n)
cnt = 0
_string = ''
for _ in range(n):
    _string = input()
    if A == _string:
        cnt += 1

print(cnt)


#    2

# 최대 10회 반복합니다.
for _ in range(10):
    # 문자열을 입력받습니다.
    string = input()

    # str이 END일 경우 종료합니다.
    if string == "END":
        break

    # 문자열의 길이를 구합니다.
    leng = len(string)

    # 문자열을 역으로 출력합니다.
    for i in range(leng - 1, -1, -1):
        print(string[i], end="")
    print()
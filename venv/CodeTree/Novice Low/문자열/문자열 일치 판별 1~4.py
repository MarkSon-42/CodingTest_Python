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


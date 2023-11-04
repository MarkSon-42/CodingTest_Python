
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n

for i in range(n):
    a[i] -= b
    if a[i] > 0:
        if a[i] % c > 0:
            answer += a[i] // c + 1
        else:
            answer += a[i] // c

print(answer)
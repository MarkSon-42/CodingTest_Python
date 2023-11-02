a, b, c = map(int, input().split())
sum = 0
for i in range(a, b + 1):
    if i % c == 0 or i % 3 == 0:
        sum += i

print(sum)
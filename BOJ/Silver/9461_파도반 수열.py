p = [0 for i in range(100001)]

p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 100001):
    p[i] = p[i - 2] + p[i - 3]

t = int(input())
for i in range(t):
    n = int(input())
    print(p[n])

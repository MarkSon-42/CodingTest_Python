t = int(input())
answer = 0

def steps(n ,p):
    a = (p+1)//2
    b = (n-p)//2

    return a + b
for i in range(t):
    n, p = map(int,input().split())
    print(steps(n, p))




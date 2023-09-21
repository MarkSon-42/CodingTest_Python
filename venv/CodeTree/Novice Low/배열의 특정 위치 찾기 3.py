nl = list(map(int, input().split()))

for i in range(len(nl)):
    if nl[i] == 0:
        print(sum(nl[i-3:i]))
        break
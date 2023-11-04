n = int(input())
evennumlist = []
num_list = list(map(int, input().split()))
for num in num_list:
    if num % 2 == 0:
        evennumlist.append(num)


reversedeven = evennumlist[::-1]
for c in reversedeven:
    print(c, end=' ')
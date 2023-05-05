import re
num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    l = input().split()
    r = input().split()

    result = []
    for j in range(len(r)):
        ch = 0
        tt = r[j].replace('.', '.{1,'+str(b)+'}')
        tt = "^"+tt+"$"
        regex = re.compile(tt)
        for q in l:
            if regex.match(q):
                result.append("#"*len(r[j]))
                ch = 1
                break
        if ch == 0:
            result.append(r[j])
    for j in range(len(result)):
        if j == len(result)-1:
            print(result[j])
        else:
            print(result[j], end=" ")







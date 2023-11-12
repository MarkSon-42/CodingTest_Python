#

n = int(input())
arr = list(map(str, input().split()))
q = int(input())
for _ in range(q):
    cnt = 0
    query = input().split()
    if query[0] == '1':
        find_arr = arr[int(query[1]) - 1:int(query[2]) - 1]
        for c in find_arr:
            if query[3] == c:
                cnt += 1
        print(cnt)
    else:
        continue

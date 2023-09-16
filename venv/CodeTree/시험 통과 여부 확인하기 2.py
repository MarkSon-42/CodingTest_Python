cnt = 0
n = int(input())
for _ in range(n):
    score_list = list(map(int, input().split()))
    average = float(sum(score_list) / len(score_list))
    if average >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')

print(cnt)
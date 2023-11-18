# 음 이건 근데 dx, dy는 아닌.. 듯?

t = int(input())
for tc in range(1, t + 1):
    sum_list = []
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        sum_val = 0
        for j in range(100):
            sum_val += arr[i][j]
        sum_list.append(sum_val)

    for j in range(100):
        sum_val = 0
        for i in range(100):
            sum_val += arr[i][j]
        sum_list.append(sum_val)

    for i in range(100):
        sum_val = 0
        sum_val += arr[i][i]
        sum_list.append(sum_val)

    for i in range(100):
        sum_val = 0
        sum_val += arr[i][99 - i]
        sum_list.append(sum_val)

    print(f"#{tc} {max(sum_list)}")

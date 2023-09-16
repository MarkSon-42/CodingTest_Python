over_list = []
_sum = 0
over_sum = 0
flag = 0
num_arr = list(map(int, input().split()))

for i in range(len(num_arr)):
    if num_arr[i] > 250:
        over_list = num_arr[:i]
        over_sum = sum(over_list)
        print(over_sum, round(over_sum/i, 1))
        flag = 1
        break
    else:
        _sum += num_arr[i]

if flag == 0:
    print(_sum, round(_sum/10, 1))

# ref : https://freedeveloper.tistory.com/393

# tow pointer algorithm

# 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘

n = 5 # 데이터 개수
m = 5 # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)



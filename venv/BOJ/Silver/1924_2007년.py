day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "TUE", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x - 1):
    day += month[i]

day = (day + y) % 7

print(week[day])


# optimization with chatGPT


month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_days = ["SUN", "MON", "TUE", "WED", "TUE", "FRI", "SAT"]

x, y = map(int, input().split())

# 굳이 반복문 돌면서 더할 필요가 없는 것...  sum()과 slicing으로 해결..!
total_days = sum(month_days[:x-1]) + y - 1
day_index = total_days % 7

print(week_days[day_index])



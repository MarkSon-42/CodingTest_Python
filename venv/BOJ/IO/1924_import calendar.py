import calendar

week = ["MON", "TUE", "WED", "TUE", "FRI", "SAT", "SUN"]

x, y = map(int, input().split())

day = calendar.weekday(2007, x, y)
print(week[day])
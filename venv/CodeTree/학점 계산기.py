
n = int(input())

f_score = list(map(float, input().split()))

_sum = sum(f_score)

score = _sum / n
grade = ''

if score >= 4.0:
    grade = 'Perfect'
elif score < 4.0 and score >= 3.0:
    grade = 'Good'
else:
    grade = 'Poor'

print(round(score, 1))
print(grade)


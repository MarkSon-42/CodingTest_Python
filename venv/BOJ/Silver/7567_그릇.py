dish = input()
answer = 10
for i in range(len(dish)-1):
    if dish[i] == dish[i+1]: # 포개지는 경우를 조건문으로 처리하면 그냥 끝나는 문제.
        answer += 5
    else:
        answer += 10

print(answer)
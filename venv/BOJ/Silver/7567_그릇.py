dish = input()
answer = 10
for i in range(len(dish)-1):
    if dish[i] == dish[i+1]:
        answer += 5
    else:
        answer += 10

print(answer)
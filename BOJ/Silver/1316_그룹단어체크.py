n = int(input())

group_word_count = n
for _ in range(n):
    word = input()
    is_group_word = True
    for i in range(len(word)):
        if i != len(word)-1 and word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]: # <- 해당 라인을 구현할 수 있느냐 없느냐가 키 포인트... 요소의 중복을 이렇게 검사!
            is_group_word = False
            break
    if not is_group_word:
        group_word_count -= 1
print(group_word_count)

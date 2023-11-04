word = input()
n = int(input())
if n > len(word):
    print(word[::-1])
else:
    word = word[len(word) - n:]
    for i in range(len(word) - 1 , -1, -1):
        print(word[i], end='')
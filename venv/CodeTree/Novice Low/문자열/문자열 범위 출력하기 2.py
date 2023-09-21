word = input()
n = int(input())

word = word[len(word) - n:]

for i in range(len(word) - 1 , -1, -1):
    print(word[i], end='')
n, m = map(int, input().split())

answer = []

def dfs():
    if len(answer) == m:
        for elem in answer:
            print(elem, end=' ')
        print()
        return

    for i in range(1, n + 1):
        answer.append(i)
        dfs()
        answer.pop()

dfs()
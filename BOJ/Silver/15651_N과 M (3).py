n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answer = []


def print_result():
    for elem in answer:
        if len(answer) == m:
            print(elem, end=' ')
    print()

def dfs():
    for num in arr:
        answer.append(num)
        dfs()
        answer.pop()

    print_result()


dfs()
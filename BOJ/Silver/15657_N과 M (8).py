# python의  *arguments 활용

# 여러 개의 인자를 함수로 받고자 할 때 쓰임!



answer = []
def dfs(x):
    if len(answer) == m:
        print(*answer)  # <- 그럼, 자동으로 공백을 기준으로 여러개를 출력해줌 ㄷㄷ
        return
    else:
        for i in range(x, n):
            answer.append(arr[i])
            dfs(i)
            answer.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
dfs(0)



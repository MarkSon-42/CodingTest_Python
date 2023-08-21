import sys
input = sys.stdin.readline

def solve(stair, n):
    dp = []
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])

    # 거꾸로 생각하기 _ 만약 계단을 다 올라간 시점에서 문제를 바라본다면?
    for i in range(3, n):
        dp.append(max(dp[i - 2] + stair[i] + dp[i - 3], stair[i] + dp[i - 2]))

    print(dp[-1])

if __name__ == '__main__':
    stair = []
    n = int(input().strip())
    for i in range(n):
        stair.append(int(input().strip()))

    solve(stair, n)
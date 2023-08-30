# DP
def solution(n):
    if n < 3:
        return n
    dp = [0] * (n + 1)
    print(dp)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567

solution(5)

# 4
# 1 1 1 1
# 1 2 1
# 1 1 2
# 2 1 1
# 2 2

# 중복있는 더하기 가짓수..인데
# < 3
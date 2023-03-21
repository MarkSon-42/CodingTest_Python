# DP : Bottom-Up (for문 사용)

x = int(input())
dp = [0] * (x+1) # dp리스트인 d를 0이 (x + 1)개 있는 리스트로 초기화 함.
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])

# 약간 두루뭉실하게 이해가 되긴 했는데, 역시나 종이나 패드에 꼭 쓰면서 설명해봐야 할 것 같다.
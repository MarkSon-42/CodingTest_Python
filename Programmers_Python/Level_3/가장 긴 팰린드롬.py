def solution(s):
    n = len(s)  # 문자열의 길이
    dp = [[False] * n for _ in range(n)]  # n x n 크기의 2차원 리스트 초기화
    max_length = 0  # 팰린드롬의 최대 길이

    for gap in range(n):
        for start in range(n):
            end = start + gap  # end는 start에서 gap만큼 떨어진 위치

            if end >= n:  # end가 문자열의 범위를 벗어나면 반복 중지
                break

            # 길이가 1 또는 2인 부분 문자열의 경우
            if gap < 2:
                if s[start] == s[end]:  # 문자열의 시작과 끝이 같으면
                    dp[start][end] = True  # 팰린드롬
            # 길이가 3 이상인 부분 문자열의 경우
            else:
                if s[start] == s[end] and dp[start+1][end-1]:  # 문자열의 시작과 끝이 같고, 내부 부분 문자열이 팰린드롬이면
                    dp[start][end] = True  # 팰린드롬

            if dp[start][end]:  # 팰린드롬이면
                max_length = max(max_length, gap + 1)  # 최대 길이 갱신

    return max_length
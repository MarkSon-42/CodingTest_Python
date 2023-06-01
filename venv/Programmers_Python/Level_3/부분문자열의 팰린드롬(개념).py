# s의 모든 부분 문자열 팰린드롬 개수를 구하는 함수
def count_substring_pal(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
m, n, k = map(int, input().split())
for _ in range(k):
    x, y = tuple(map(int, input().split()))


# graph라는 2차원 배열에 통합하는 연습부터
# visited까지 선언해서 가장 정석적인 풀이 ㄱ

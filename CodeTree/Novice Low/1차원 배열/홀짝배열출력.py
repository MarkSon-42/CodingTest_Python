#
# 문제
# n개의 수로 이루어진 수열 a, b가 있습니다. 이 때, 수열 b의 홀수번째 수들을 뒤에서부터 역순으로 출력한 뒤 수열 a의 짝수번째 수들을 순서대로 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 n이 주어집니다.
# 두 번째 줄에 수열 a의 원소 n개가 공백을 사이에 두고 주어집니다.
# 세 번째 줄에 수열 b의 원소 n개가 공백을 사이에 두고 주어집니다.
#
# 1 ≤ n ≤ 100
# 1 ≤ 주어지는 정수 ≤ 100
# 출력 형식
# 첫 번째 줄에 수열 a, b의 특정 조건을 만족하는 숫자들을 공백을 사이에 두고 출력합니다.
#
# 먼저 주어진 숫자들 중 수열 b의 홀수번째 수들을 역순으로 전부 출력한 뒤 이어서 수열 a의 짝수번째 수들을 주어진 순서대로 전부 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 5
# 1 2 3 4 5
# 4 6 7 8 10
# 출력:
#
# 10 7 4 2 4
# 예제2
# 입력:
#
# 6
# 6 5 4 3 2 1
# 1 2 3 4 5 6
# 출력:
#
# 5 3 1 5 3 1
# 예제 설명
# 첫 번째 예제에서 수열 b의 홀수번째 수는 순서대로 4, 7, 10, 그리고 수열 a의 짝수번째 수는 순서대로 2, 4 입니다. 따라서 답은 10 7 4 2 4가 됩니다.
#
# 첫 번째 예제에서 수열 b의 홀수번째 수는 순서대로 1, 3, 5, 그리고 수열 a의 짝수번째 수는 순서대로 5, 3, 1 입니다. 따라서 답은 5 3 1 5 3 1이 됩니다.




n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = b.sort(reverse = True)
for i in range(len(b),0,2):
    print(b[i], end = ' ')
for i in range(len(a)):
    if i % 2 != 0:
        print(a[i], end = ' ')


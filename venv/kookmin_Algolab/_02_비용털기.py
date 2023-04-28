t = int(input())

n, p = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() # 새로운 정렬된 객체를 만들어줌
a = 0
b = n-1
for _ in range(len(nums)):
    sum_two = nums[a] + nums[b]
    if sum_two == p:
        print(nums[a], nums[b])
        break
    elif sum_two < p:
        a += 1
    else:
        b -= 1

# 숲가꾸기

import sys

t = int(input())
for z in range(t):
    n, c, k, p = map(int, input().split())

    forest = []
    trees = []

    for i in range(n):
        temp1 = []
        for j in range(n):
            temp2 = []
            temp1.append(temp2)
        trees.append(temp1)

    for i in range(n):
        temp = list(map(int, sys.stdin.readline().strip().split()))
        forest.append(temp)

    for i in range(c):
        temp = list(map(int, sys.stdin.readline().strip().split()))
        trees[temp[0]][temp[1]].append(temp[2])

    for o in range(p):

        for i in range(n):
            for j in range(n):
                tree = sorted(trees[i][j])
                for l in range(len(tree)):
                    if forest[i][j] < tree[l]:
                        for a in range(l, len(tree)):
                            forest[i][j] += tree[a] // 2
                        tree = tree[:l]
                        trees[i][j] = tree
                        break
                    else:
                        forest[i][j] -= tree[l]
                        tree[l] += 1
                else:
                    trees[i][j] = tree

        for i in range(n):
            for j in range(n):
                tree = trees[i][j]
                for l in tree:
                    if l % 5 == 0:
                        if i - 1 >= 0 and j - 1 >= 0:
                            trees[i - 1][j - 1].append(1)
                        if j - 1 >= 0:
                            trees[i][j - 1].append(1)
                        if i + 1 < n and j - 1 >= 0:
                            trees[i + 1][j - 1].append(1)
                        if i + 1 < n:
                            trees[i + 1][j].append(1)
                        if i + 1 < n and j + 1 < n:
                            trees[i + 1][j + 1].append(1)
                        if j + 1 < n:
                            trees[i][j + 1].append(1)
                        if i - 1 >= 0 and j + 1 < n:
                            trees[i - 1][j + 1].append(1)
                        if i - 1 >= 0:
                            trees[i - 1][j].append(1)

        for i in range(n):
            for j in range(n):
                forest[i][j] += k

    answer = 0
    for i in range(n):
        for j in range(n):
            answer += len(trees[i][j])

    print(answer)

    ########################################################

    # 사다리 타기

    t = int(input())
X = [-1, 1]

for i in range(t):
    n, m, d = map(int, input().split())
    data = [list(input()) for _ in range(m)]

    for j in range(len(data) - 1, -1, -1):
        now_d = 2 * d - 2
        next_d = d
        for k in X:
            if 0 <= now_d + k < (2 * n - 1) and data[j][now_d + k] == '+':
                next_d = d + k
        d = next_d

    print(d)

# 비용털기


t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    a = 0
    b = n - 1
    for _ in range(n):
        sum = num[a] + num[b]
        if (sum == p):
            print(num[a], num[b])
            break
        elif (sum < p):
            a += 1
        else:
            b -= 1

# 건물

num = int(input())
for i in range(num):
    re = 0
    chk = 0
    t = input()
    l = list(map(int, input().split()))
    for a in range(len(l)):
        if chk < l[-1]:
            re += 1
            chk = l[-1]
        l.pop(-1)
    print(re)

# 막대기 분할

import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    s = input().rstrip()
    stack = []
    cnt = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')

        else:  # ')'
            if s[i - 1] == '(':  # Razor
                stack.pop()
                cnt = cnt + len(stack)

            else:  # ')', ironBar
                cnt += 1
                stack.pop()
    print(cnt)

# 공장

t = int(input())

for cnt in range(t):  # 왜 증감 인덱스가 cnt인지??
    n = int(input())
    A, B = [], []  # 공장 A와 B에 주문한 제품 개수를 저장하는 리스트
    sum_a, sum_b = 0, 0  # 각각 가게에 주문한 총 개수를 저장

    for _ in range(n):
        a = input()  # 처리해야할 주문
        if a[0] == 'O':
            ord, cnt, fac = a.split()  # 공백을 기준으로 ord, cnt, fac 각각 할당
        else:
            ord, fac = a.split()

        if ord == "ORDER":  # ORDER일 경우, fac(공장이름)과,  cnt(주문량) 파싱
            if fac == 'A':  # 주문 할당 공장이 A인 경우
                A.append(int(cnt))
                sum_a += int(cnt)
            elif fac == 'B':  # 주문 할당 공장이 B인 경우
                B.append(int(cnt))
                sum_b += int(cnt)
            else:  # 주문 할당 공장이 C인 경우
                if sum_a <= sum_b:
                    A.append(int(cnt))
                    sum_a += int(cnt)
                else:
                    B.append(int(cnt))
                    sum_b += int(cnt)
        else:
            if fac == 'A':
                sum_a -= A.pop(0)
            else:
                sum_b -= B.pop(0)
    print(sum_a, sum_b)

#   계단 오르기

t = int(input())  # 테케 입력받고,

for _ in range(t):  # 테스트케이스 수만큼 입력받기
    n, p = map(int, input().split())  # n과 p를 입력받기. n은 계단의 총 수 , p는 망가진 계단의 위치.

    if n % 2 == 0:
        if p % 2 == 0:
            print((n // 2) + 1)
        else:
            print(n // 2)
    else:
        print((n // 2) + 1)

# 수고르기


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    diff = 1000000000
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = nums[j] - nums[i]
            if m <= d < diff:
                diff = d
                break
        if diff == m:
            break
    print(diff)

#  필터링

import re

# 테스트 케이스의 개수를 입력받음
num = int(input())

for i in range(num):
    # a, b, l, r 값을 입력받음
    a, b = map(int, input().split())
    l = input().split()
    r = input().split()

    result = []
    for j in range(len(r)):
        ch = 0
        # .을 .{1,b}로 변경하여 정규식 패턴을 만듦
        tt = r[j].replace('.', '.{1,' + str(b) + '}')
        # 패턴의 시작과 끝을 나타내는 ^와 $를 추가함
        tt = "^" + tt + "$"
        # 패턴을 컴파일하여 정규식 객체를 생성함
        regex = re.compile(tt)
        for q in l:
            # 정규식 객체를 사용하여 패턴에 맞는 문자열을 찾음
            if regex.match(q):
                # '#'으로 이루어진 문자열을 결과 리스트에 추가함
                result.append("#" * len(r[j]))
                ch = 1
                break
        if ch == 0:
            # 패턴에 맞는 문자열이 없는 경우, 원래 문자열을 결과 리스트에 추가함
            result.append(r[j])
    for j in range(len(result)):
        # 리스트의 마지막 요소인 경우, 개행 없이 출력함
        if j == len(result) - 1:
            print(result[j])
        # 리스트의 마지막 요소가 아닌 경우, 한 칸 띄어쓰기를 하여 출력함
        else:
            print(result[j], end=" ")

#   재택근무


t = int(input())
for i in range(t):
    i, k, j, l = map(int, input().split())
    team = []
    teamt = []

    can = input().split()
    cant = input().split()

    for w in range(i):
        team.append([])
        teamt.append([])
    result = []

    for w in range(l):
        team_n, num = map(int, input().split())
        tmp = input().split()
        check = 0
        for q in cant:
            if q in tmp:
                check = 1
                break
        if check == 0:
            team[team_n - 1].append(w + 1)
        else:
            teamt[team_n - 1].append(w)

    for w in range(i):
        if teamt[w] == []:
            team[w][0] = -1
    for w in range(i):
        for q in team[w]:
            if q != -1:
                result.append(q)

    result.sort()

    if result == []:
        print(-1)
    else:
        print(" ".join(map(str, result)))

# 레전드 매치


import sys

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    status = sorted(map(int, sys.stdin.readline().split()), reverse=True)
    if n % 2 == 1:
        status.append(0)
        n += 1
    delta = sorted([(status[i] - status[i + 1], i) for i in range(0, n, 2)], reverse=True)
    for i in range(m):
        index = delta[i][1]
        status[index], status[index + 1] = status[index + 1], status[index]
    print(sum(status[1:n:2]))



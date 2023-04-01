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


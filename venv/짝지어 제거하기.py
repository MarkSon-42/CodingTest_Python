def solution(s):
    stack = [] #  스택 초기화

    for i in range(len(s)):
        if stack and stack[-1] == s[i]: # 스택 탑(stack[-1])이랑 stack값이 같으면
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        return 0
    else:
        return 1
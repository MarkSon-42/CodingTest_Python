t = int(input())

for _ in range(t):

    stick = input()  # ()))(()..  괄호들을 입력받는다. 문자열.
    stack = []  # 스택을 쓸꺼면 선언해라~
    answer = 0  # 결과값 초기화

    # while start
    i = 0  # while문 시작 : 인덱스 초기화 부터~
    while i != len(stick):  # 문자열 stick의 길이만큼 반복한다는 의미. i가 ++되어서 문자열 길이만큼 가면 종료!
        if stick[i] == '(' and stick[i + 1] == ')':  # 레이저인 경우
            answer += len(stack)  # 스택에 있는 쇠막대기 개수만큼 결과값에 추가
            i += 1  # 다음 문자로 이동
        elif stick[i] == '(':  # 여는 괄호인 경우 스택에 push -> 막대기를 의미?
            stack.append(1)
        elif stick[i] == ')':
            stack.pop()
            answer += 1
        i += 1

    print(answer)

# def solution(s):
#     answer = 0
#     temp = list(s)
def solution(s):
    answer = 0
    temp = list()
    for _ in range(len(s)):

#     # 리스트의 길이만킅 for문을 돌려 리스트 회전
#     for _ in range(len(s)):
#         stack = []
#         #         스택에 아무것도 없으면 괄호를 추가 같으면 제거
#         for j in range(len(temp)):
#             if len(stack) > 0:
#                 if stack[-1] == "(" and temp[j] == ")":
#                     stack.pop()
#                 elif stack[-1] == "[" and temp[j] == "]":
#                     stack.pop()
#                 elif stack[-1] == "{" and temp[j] == "}":
#                     stack.pop()
#                 #                 만약에 마지막에 있는 문자가 다르면 추가
#                 else:
#                     stack.append(temp[j])
#             #             길이가 0이면 추가
#             else:
#                 stack.append(temp[j])
#         #         for문 다 돌았는데 길이 0 이면 정답하나 추가
#         if len(stack) == 0:
#             answer += 1
#         #         첫번째꺼 맨뒤로 보내고 다시 위에꺼 반복
#         temp.append(temp.pop(0))
#
#     return answer

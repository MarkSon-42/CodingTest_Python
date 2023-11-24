# stack
def solution(board, moves):
    answer = 0
    stack = []
    pick = 0
    for i in moves:
        for j in range(len(board) - 1, 0, -1):
            if board[i][j] != 0:
                pick = board[i][j]
            if stack and stack[-1] == pick:
                stack.pop()
                answer += 1
            else:
                stack.append(pick)

    return answer

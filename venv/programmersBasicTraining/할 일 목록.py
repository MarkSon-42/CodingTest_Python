def solution(todo_list, finished):
    unfinished_tasks = []  # 미완료된 작업들을 담을 배열

    for i in range(len(todo_list)):
        if not finished[i]:  # 해당 작업이 완료되지 않았을 경우
            unfinished_tasks.append(todo_list[i])

    return unfinished_tasks

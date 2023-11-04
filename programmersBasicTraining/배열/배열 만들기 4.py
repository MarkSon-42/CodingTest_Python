def solution(arr):
    stk = []  # stk: 새로운 배열
    i = 0  # 인덱스 변수 i 초기화
    while i < len(arr):  # i가 arr의 길이보다 작을 때까지 반복
        if not stk:  # stk가 비어있는 경우
            stk.append(arr[i])  # arr[i]를 stk에 추가
            i += 1  # i에 1을 더함
        elif stk[-1] < arr[i]:  # stk에 요소가 있고, stk의 마지막 요소가 arr[i]보다 작은 경우
            stk.append(arr[i])  # arr[i]를 stk에 추가
            i += 1  # i에 1을 더함
        else:  # stk에 요소가 있고, stk의 마지막 요소가 arr[i]보다 크거나 같은 경우
            stk.pop()  # stk에서 마지막 요소를 제거
    return stk  # 생성된 stk 반환



def solution2(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk
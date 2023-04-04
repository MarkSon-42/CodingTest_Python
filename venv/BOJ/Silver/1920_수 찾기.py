# N = int(input())
# N_nums = sorted(list(map(int, input().split())))
# M = int(input())
# M_nums = list(map(int, input().split()))

# for i in range(len(M_nums)):
#     if M_nums[i] in N_nums:
#         print(1)
#     else:
#         print(0)

# 해당 코드는 가차없이 시간초과. 자료구조를 쓰지 않았기 때문.
# solution ref : https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python

N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))

N_nums.sort() # 원본 N_nums의 값을 정렬된 상태로 수정

# N nums의 각 원소별로 이분탐색을 해야한다.
for num in M_nums:
    left_element, right_element = 0, N - 1
    isExist = False # 찾았는지 여부

    # start binary search
     while left_element <= right_element:
         mid = (left_element + right_element) // 2
         if num == N_nums[mid]:
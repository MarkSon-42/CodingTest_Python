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

N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))

N_nums.sort() # 원본 N_nums의 값을 정렬된 상태로 수정

# N nums의 각 원소별로 이분탐색을 해야한다.



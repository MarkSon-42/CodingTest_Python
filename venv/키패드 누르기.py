# 키패드 한칸은 거리 1, 대각선 거리같은거 없음
# 조건문 처리
# 거리가 가깝다, 멀다,
# 거리가 같다 -> == 'left' ? =='right'
# *, # 은 따로 다룰게 아니라 그냥 숫자로 바꿔야 할듯?
# 0도 바꿔버려야 함. 0 때문에 조건 더늘어남.
# 1 2 3 4 5 6 7 8 9  ->  10 11 12
#                        *  0   #

def solution(numbers, hand):
    answer = ''

    r_location = 12
    l_location = 10
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            print('L')
            l_location = i
            print(i)
        elif i == 3 or i == 6 or i == 9:
            print('R')
            r_location = i
            print(i)
        else:  # 2, 5, 8, 0에 대한 처리를 해야함.. 현재 키패드의 위치는 어떻게?
            # 누가 더 거리가 먼지 어떻게 따질 수 있지?
            # 그냥 2차원 배열을 써야하나? (x)
            # 거리는 0, 1, 2, 3, 4 중 하나임. (숫자를 빼보면 된다)
            # i = 2,5,8,0 일때 l_loaction이 가까운지, r_location이 가까운지 판별하기
            if i == 0:
                i = 11

            left_tmp = abs(l_location - i)
            right_tmp = abs(r_location - i)

            left_dist = (left_tmp / 3) + (left_tmp % 3)
            right_dist = (right_tmp / 3) + (right_tmp % 3)

    return answer
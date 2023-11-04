# 문제 풀이 출처 : https://somjang.tistory.com/entry/Programmers-%EC%97%B0%EC%86%8D%EB%90%9C-%EC%88%98%EC%9D%98-%ED%95%A9-Python
# 1. 규칙 찾기
# 가운데 또는 가운데 왼쪽에 들어가는 숫자 구하기

def get_middle_num(num, total):
    return total // num # num이 짝수일 경우에는 몫만 구하니까 해당 리턴 값은 가운데에서 왼쪽으로 한칸

def solution(num, total):
    middle_idx = num // 2
    middle_num = get_middle_num(num, total)

    start_num = middle_idx * -1 if num % 2 == 1 else middle_idx * -1 + 1
    end_num = middle_idx + 1

    answer = [num + middle_num for num in range(start_num, end_num)]

    return answer 
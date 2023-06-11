def solution(num_list):
    odd_sum = 0  # 홀수 번째 요소들의 합을 저장하는 변수
    even_sum = 0  # 짝수 번째 요소들의 합을 저장하는 변수

    for i in range(len(num_list)):
        if i % 2 == 0:  # 홀수 번째 요소인 경우
            odd_sum += num_list[i]
        else:  # 짝수 번째 요소인 경우
            even_sum += num_list[i]

    if odd_sum >= even_sum:
        return odd_sum
    else:
        return even_sum

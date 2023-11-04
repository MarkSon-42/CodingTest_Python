def solution(bin1, bin2):
    carry = 0  # 이진수 덧셈에서의 자리올림을 나타내는 변수
    result = []  # 결과를 저장할 리스트

    i = len(bin1) - 1  # bin1의 마지막 자리 인덱스
    j = len(bin2) - 1  # bin2의 마지막 자리 인덱스

    # bin1과 bin2를 덧셈하고 결과를 result에 저장
    while i >= 0 or j >= 0 or carry == 1:
        sum_ = carry  # 자리올림을 더해줌

        # bin1의 현재 자리의 숫자를 더함
        if i >= 0:
            sum_ += int(bin1[i])
            i -= 1

        # bin2의 현재 자리의 숫자를 더함
        if j >= 0:
            sum_ += int(bin2[j])
            j -= 1

        result.append(str(sum_ % 2))  # 현재 자리의 이진수를 결과 리스트에 추가
        carry = sum_ // 2  # 다음 자리의 자리올림을 결정

    result.reverse()  # 결과 리스트를 역순으로 정렬

    return ''.join(result)  # 결과 리스트를 이진수 문자열로 변환하여 반환

def solution(a, b, c, d):
    # 주어진 숫자들을 리스트로 저장합니다.
    nums = [a, b, c, d]

    # 각 숫자의 개수를 세어 리스트로 저장합니다.
    counts = [nums.count(i) for i in nums]

    # 가장 많이 등장한 숫자의 개수를 확인합니다.
    if max(counts) == 4:
        # 만약 가장 많이 등장한 숫자의 개수가 4라면, 해당 숫자에 1111을 곱한 값을 반환합니다.
        return a * 1111
    elif max(counts) == 3:
        # 만약 가장 많이 등장한 숫자의 개수가 3이라면,
        # 하나는 다른 숫자와 세트를 이루기 위해 3개의 숫자 중 하나를 선택하고,
        # 나머지 하나는 다른 숫자와 세트를 이루지 않기 위해 1개의 숫자를 선택합니다.
        p = nums[counts.index(3)]  # 세트를 이루는 숫자 p를 선택합니다.
        q = nums[counts.index(1)]  # 세트를 이루지 않는 숫자 q를 선택합니다.
        return (10 * p + q) ** 2  # (10p + q)의 제곱을 반환합니다.
    elif max(counts) == 2:
        # 만약 가장 많이 등장한 숫자의 개수가 2라면,
        if min(counts) == 2:
            # 모든 숫자들이 2번 등장한다면, 두 쌍의 숫자를 선택하여 계산합니다.
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
            # 만약 a와 b가 같다면, a와 c의 차이를 이용하여 계산합니다.
            # 그렇지 않으면 a와 b의 차이를 이용하여 계산합니다.
        else:
            # 두 숫자 쌍 중 하나가 2번 등장하고 다른 숫자들은 각각 1번 등장한다면,
            # 2번 등장하는 숫자를 선택하여 나머지 숫자들의 곱을 나눕니다.
            p = nums[counts.index(2)]
            return (a * b * c * d) / p ** 2
    else:
        # 모든 숫자들이 각각 1번씩 등장한다면, 가장 작은 숫자를 반환합니다.
        return min(nums)

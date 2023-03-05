# 뭔가 멋지게 풀 수도 있을꺼 같은데 일단 가장 단순하게 접근하자면

# 수열이 주어지면 등차수열인지 등비수열인지 확인하고 전자의 경우 등차를 구하고 후자의 경우 등비를 구한다

# 마지막 원소에 앞서 구한 등차를 더하거나, 등비를 곱해주면 끝.

def solution(common):
    answer = 0
    if common[1] - common[0] != common[2] - common[1]:  # 연속된 항의 길이가 다르면 이건 등차수열이 아님. 고로 등비수열
        return common[1] // common[0] * common[len(common) - 1]
    else:
        return common[1] - common[0] + common[len(common) - 1]

        # 처음에 common[len(common)]에 -1을 안해줘서 한번 틀림..
ㅎ
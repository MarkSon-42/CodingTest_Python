# 테스트 케이스의 개수를 입력받습니다.
t = int(input())
for _ in range(t):
    # 각 테스트 케이스에 대한 카드의 개수를 입력받습니다.
    n = int(input())

    # 1부터 n까지의 합을 구합니다.
    total_sum = n * (n + 1) // 2

    # 쿠민이가 가지고 있는 카드의 숫자들을 입력받습니다.
    cards = list(map(int, input().split()))

    # 가지고 있는 카드의 숫자들의 합을 구합니다.
    cards_sum = sum(cards)

    # 1부터 n까지의 합에서 가지고 있는 카드의 숫자들의 합을 빼서 잃어버린 카드의 번호를 찾습니다.
    lost_card = total_sum - cards_sum

    # 잃어버린 카드의 번호를 출력합니다.
    print(lost_card)

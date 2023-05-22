def solve(n, m, k, cards):
    # 카드를 그룹으로 나눕니다.
    groups = []
    for i in range(m):
        if i == 0 or cards[i] != cards[i - 1] + 1:
            groups.append([cards[i]])
        else:
            groups[-1].append(cards[i])

    # 카드를 하나씩 선택합니다.
    scores = []
    for i in range(k):
        score = 0
        for group in groups:
            score += min(group)
        scores.append(score)

    # 결과를 출력합니다.
    for score in scores:
        print(score, end=" ")
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        cards = list(map(int, input().split()))
        solve(n, m, k, cards)

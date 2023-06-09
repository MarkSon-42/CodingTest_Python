def smallest_prime(n):
    # n이 소수인지 확인하는 함수
    if n == 2 or n == 3: return n
    if n % 2 == 0: return 2
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return i
    return n

def shuffle_cards(cards):
    # 카드 섞는 함수
    if len(cards) == 1:
        return cards
    prime = smallest_prime(len(cards))  # 소수 찾기
    if prime == len(cards):
        return cards
    shuffled = []
    for i in range(prime):
        shuffled.extend(shuffle_cards(cards[i::prime]))  # 카드를 나누고 재귀 호출
    return shuffled

# 메인 함수
t = int(input())
for _ in range(t):
    n = int(input())
    cards = [i+1 for i in range(n)]
    result = shuffle_cards(cards)
    print(' '.join(map(str, result)))

# 1. 거스름돈 문제 (최소 동전 갯수)

def change_money(price, payment):
    change = payment - price
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        count += change // coin
        change %= coin
    return count


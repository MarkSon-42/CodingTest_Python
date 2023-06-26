def solution(order):
    menu_price = {
        "iceamericano": 4500,
        "americanoice": 4500,
        "hotamericano": 4500,
        "americanohot": 4500,
        "icecafelatte": 5000,
        "cafelatteice": 5000,
        "hotcafelatte": 5000,
        "cafelattehot": 5000,
        "americano": 4500,
        "cafelatte": 5000,
        "anything": 4500
    }

    total_payment = 0

    for item in order:
        total_payment += menu_price[item]

    return total_payment
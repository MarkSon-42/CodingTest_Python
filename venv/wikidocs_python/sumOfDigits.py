# 입되는 숫자의 각 자릿수를 더하는 함수 구현 _ 리스트를 이용해서 푸는 방식

def sumOfDigits(num):
    sum = 0
    for c in list(str(num)): #반복문에서 list로 변환.
        sum += int(c)

    return sum


if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))



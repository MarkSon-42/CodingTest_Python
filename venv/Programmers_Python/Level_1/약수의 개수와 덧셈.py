def calculate_sum(left, right):
    total_sum = 0

    for num in range(left, right + 1):
        divisors_count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors_count += 1

        if divisors_count % 2 == 0:
            total_sum += num
        else:
            total_sum -= num

    return total_sum
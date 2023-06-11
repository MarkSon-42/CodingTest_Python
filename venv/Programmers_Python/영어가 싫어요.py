def solution(numbers):
    words = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

    for idx, num in enumerate(words):
        numbers = numbers.replace(num, str(idx))

    return int(numbers)
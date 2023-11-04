def solution(myString):
    lengths = []
    current_length = 0

    for char in myString:
        if char == "x":
            lengths.append(current_length)
            current_length = 0
        else:
            current_length += 1

    lengths.append(current_length)

    return lengths

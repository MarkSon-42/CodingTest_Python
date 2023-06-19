def solution(strArr):
    group_counts = {}
    for word in strArr:
        length = len(word)
        if length in group_counts:
            group_counts[length] += 1
        else:
            group_counts[length] = 1
    max_count = max(group_counts.values())
    return max_count



def solution2(strArr):
    a = [0] * 31
    for x in strArr: a[len(x)] += 1
    return max(a)
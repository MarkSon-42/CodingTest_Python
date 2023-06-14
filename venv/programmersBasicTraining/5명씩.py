def solution(names):
    front_people = []
    groups = len(names) // 5

    for i in range(groups):
        front_people.append(names[i * 5])

    if len(names) % 5 > 0:
        front_people.append(names[groups * 5])

    return front_people

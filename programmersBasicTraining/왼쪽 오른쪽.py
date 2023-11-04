def solution(str_list):
    if "l" in str_list and "r" in str_list:
        l_index = str_list.index("l")
        r_index = str_list.index("r")
        if l_index < r_index:
            return str_list[:l_index]
        else:
            return str_list[r_index+1:]
    elif "l" in str_list:
        index = str_list.index("l")
        return str_list[:index]
    elif "r" in str_list:
        index = str_list.index("r")
        return str_list[index+1:]
    else:
        return []


def solution2(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []

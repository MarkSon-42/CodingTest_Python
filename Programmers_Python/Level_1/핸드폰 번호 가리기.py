def solution(phone_number):
    length = len(phone_number)
    back = phone_number[-4:]
    return "*"*(length-4)+back
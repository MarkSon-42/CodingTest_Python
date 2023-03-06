# 반복문이건 해시건 어쨌든 해당 문제를 풀면서 적어도 3개의 출력값에 대한 조건문 구조는
# 머릿속이나 종이에 반드시 결론을 내고 코드를 짰어야 했다.

def solution(id_pw, db):
    db_dict = {i[0]: i[1] for i in db}

    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
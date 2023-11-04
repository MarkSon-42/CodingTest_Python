#  등수가 높은 순서대로 10000 × a + 100 × b + c를 return


#  https://tae-seokyoung.tistory.com/entry/0503-%EB%AC%B8%EC%9E%90%EC%97%B4%EA%B3%BC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%A3%8C%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%84%EA%B5%AD-%EB%8C%80%ED%9A%8C-%EC%84%A0%EB%B0%9C-%EA%B3%A0%EC%82%AC

#  rank index, attendance index match

#  false 제외

#  { rank : attendance }


def solution(rank, attendance):
    a = [idx for idx, v in enumerate(attendance) if v]
    b = sorted(a, key=lambda x: rank[x])

    return b[0] * 10000 + b[1] * 100 + b[2]



def solution2(rank, attendance):
    answer = 0

    rank_dict = {r: idx for idx, r in enumerate(rank)}
    weight = 4
    for r in range(1, len(rank) + 1):
        if attendance[rank_dict[r]]:
            answer += rank_dict[r] * (10 ** weight)
            weight -= 2
            if weight == -2:
                break

    return answer


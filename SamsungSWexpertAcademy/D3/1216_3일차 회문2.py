# 테스트 케이스 개수 (1부터 10까지)
for x in range(1, 11):
    # 테스트 케이스 번호를 입력받음 (실제로는 사용하지 않음)
    input()

    # 100개의 줄을 입력받아 리스트에 저장
    l = [input() for i in range(100)]

    # 리스트에 세로 줄을 추가
    l += [[l[i][j] for i in range(100)] for j in range(100)]

    # 최대 팰린드롬 길이를 1로 초기화
    r = 1

    # 팰린드롬 길이를 2부터 100까지 검사
    for i in range(2, 101):
        # 각 줄에서 시작 인덱스를 설정
        for j in range(101 - i):
            # 가로, 세로 모두 확인하기 위해 200개의 줄을 순회
            for q in range(200):
                # 팰린드롬을 발견한 경우 최대 길이를 업데이트하고 루프를 종료
                if l[q][j : j + i] == l[q][j : j + i][::-1]:
                    r = i
                    j = 100
                    break

                # 최대 길이와 현재 길이의 차이가 2 이상인 경우 루프 종료
                if i - r > 2:
                    i = j = q = 100
                    break

    # 결과 출력
    print("#%d %d" % (x, r))

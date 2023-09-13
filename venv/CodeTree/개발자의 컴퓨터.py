N = int(input())

requirements = [] #  s, t, b를
for _ in range(N):
    s, t, b = map(int, input().split())
    requirements.append((s, t,  b))

# 각 시간 지점에서 컴퓨터 사용량 저장할 딕셔너리
usage = {}

for req in requirements:
    s, t, b = req

    if s in usage:
        usage[s] += b
    else:
        usage[s] -= b

    # 시간 s에서 컴퓨터 사용량을 b만큼 증가


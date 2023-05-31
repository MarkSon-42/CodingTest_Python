def solve(line, ruler):
    sub = line - ruler

    if sub > 0 or line % 2 == 0:
        cnt = 0

        if sub > 0:
            if line / 2 != ruler:
                piece1 = ruler
                piece2 = line - ruler
                cnt += solve(piece1, ruler) * solve(piece2, ruler)
            if line % 2 == 0 or line / 2 == ruler:
                piece = line // 2
                tmp = solve(piece, ruler)
                cnt += tmp ** 2
            if sub % 2 == 0 and line / 3 != ruler:
                piece1 = sub // 2
                piece2 = line - piece1
                cnt += solve(piece1, ruler) * solve(piece2, ruler)
            return cnt
        else:
            return 1
    else:
        return 1

t = int(input())

for _ in range(t):
    line, ruler = map(int, input().split())
    print(solve(line, ruler) % 10007)
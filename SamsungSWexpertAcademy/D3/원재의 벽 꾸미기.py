t = int(input())

# A X lR – Cl + B X (N - R X C)

for tc in range(1, t + 1):
    min_val = 99999999
    n, a, b = map(int, input().split())
    for r in range(1, n + 1):
        c = 1
        while r * c <= n:
            val = a * (abs(r - c)) + b * (n - (r * c))
            min_val = min(min_val, val)
            c += 1
    print("#%d %d" % (tc, min_val))


# SWEA 출력 print('#%d %d' % (tc, min_value))

# hell

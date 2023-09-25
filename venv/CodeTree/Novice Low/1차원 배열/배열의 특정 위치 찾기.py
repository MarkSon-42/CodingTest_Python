nl = list(map(int, input().split()))
even_nl = nl[1::2]
third_nl = nl[::3]
print(sum(even_nl), round(sum(third_nl)/len(third_nl), 1))

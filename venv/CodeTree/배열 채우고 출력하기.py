chars = list(map(str, input().split()))
reversed_str = ''
for i in range(len(chars) - 1, -1, -1):
    reversed_str += chars[i]

print(reversed_str)
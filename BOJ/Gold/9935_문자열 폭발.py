import sys

# input = sys.stdin.readline

s = input()
bomb = input()
stack = []

for char in s:
    stack.append(char)
    if "".join(stack[-len(bomb) :]) == bomb:
        del stack[-len(bomb) :]

print("".join(stack) if stack else "FRULA")

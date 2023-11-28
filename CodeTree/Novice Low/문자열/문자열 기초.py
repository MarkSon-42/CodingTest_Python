# # join() : 이것은 함수..
#
# sep.join(리스트)
#
# 각 리스트내 원소들을 특정 구분값( sep )을 기준으로 합!쳐!주!는 함수
#
print(
    ",".join(["1", "2", "3"]),
    ":".join(["11", "22", "33"]),
    "".join(["a", "b", "c"]),
)


n = int(input())
str = list(input().split())

str = "".join(str)

for i in range(len(str) // 5 + 1):
    print(str[i * 5 : (i + 1) * 5])


def ispal(a, b):
    if a + b == b + a:
        return True
    else:
        return False


a = input()
b = input()

if ispal(a, b):
    print("true")
else:
    print("false")

# print("true" if ispal(a, b) else "false")

print("true" if ispal(a, b) else "false")

import re

s1 = input()
s2 = input()
s3 = s1 + s2


print(re.sub(r"\s", "", s3))
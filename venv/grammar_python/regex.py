# 정규식 표현은 문자열 패턴에 매우 유용하다.


#
#     . : matches any single character except a newline.
#     *
#     +
#     ?
#     ^
#     $
#     []
#     |

import re

pattern = r".at"

match = re.search(pattern, "The cat in the hat.")

if match:
    print("Pattern found!")


pattern = r"[aeiou]"

match = re.search(pattern, "The quick brown fox jumps over the lazxy dog.")

if match:
    print("Pattern found!")


p
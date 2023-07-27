# 파이썬 해시 공부 : https://yunaaaas.tistory.com/46

# 파이썬에서는 Dictionary 자료구조로 해시를 제공한다

# Dictionary는 dict class에 있음!

# 해시를 언제 사용하면 좋을까 ?

# 이 문제처럼 시간복잡도가 의심되는 문제는 O(1)의 시간복잡도를 가진 해시를 사용!

# empty dictionary
dict1 = {}  # {}
dict2 = dict()  # {}

print(dict1, dict2)

# key-value pair dictionary
Dog = {
    'name': 'baobao',
    'weight': 4,
    'height': 100,
}

print(Dog)

# dictionary에서 원소 가져오기

#  1. []
#  2. get()

dict3 = {
    'hi': 300,
    'hello': 180,
}

print(dict3['hello'])



# dictionary
# python.. dict class
# dict : hashmap data structure
# key : value

# key, value를 동시에 저장한다
# insert, delete, search -> O(1)

d1 = dict()

d2 = {}

d3 = {
    'A' : 3,
    'B' : 373,
    '101' : "aba"
}

# key : immutable..    list 같은건 안됨. 불변의 객체가 들어가야 함

# dict 자주 쓰이는 3가지

# d = dict()일때,

# 1. d[K] = V   : hashmap에 쌍(K, V)를 추가

# 2. d.pop(K)   : 현재 hashmap에 들어있는 데이터 중 key가 K인 쌍을 찾아 제거

# 3. K in d   : 현재 hashmap에 key가 K인 쌍이 있는지를 확인합니다. 있다면 True, 아니라면 False를 반환
 # 마찬가지 이유로 K not in d라는 구문 역시 사용 가능

d = dict()

d['banana'] = 6
d['apple'] = 2
d['cat'] = 1

if 'cat' in d:
    print(d['cat'])   # output : 1
d.pop('apple')

if 'apple' not in d:
    print('not exists!')

d['cat'] = 10
print(d['cat'])

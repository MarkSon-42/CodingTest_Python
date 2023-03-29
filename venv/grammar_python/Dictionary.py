Dict = {1 : 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)

# Nested dictionary : 딕셔너리 중첩도 가능

Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

# get() : time complexity : O(1)

print(Dict.get(3))
print(Dict.get(2))

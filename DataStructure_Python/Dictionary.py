my_dict = {}

print(my_dict)

print(type(my_dict))

my_dict_01 = dict()

print(type(my_dict_01))

# dictionary_name = {key : value}

my_info = {'name': 'Boyeon', 'age': 29, 'location': 'Seoul'}

my_info_01 = dict({'name': 'Boyeon', 'age': 29, 'location': 'Seoul'})

# fromkeys()

cities = ('Seoul', 'Paris', 'Madrid')

# fromkeys() 메서드를 통해서 'my_cities'라는 딕셔너리 생성하기

my_cities = dict.fromkeys(cities)

print(my_cities)

# 딕셔너리의 모든 키에 동일한 값을 설정하는 다른 예

# 단일 값을 생성하기

city_type = 'Capital'

my_cities = dict.fromkeys(cities, city_type)

print(my_cities)

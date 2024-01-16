my_dict = {}  # 비어있는 딕셔너리 자료형 변수 선언

print(my_dict)

print(type(my_dict))  # 타입 : 딕셔너리

my_dict_01 = dict()  # dict() 메서드로 딕셔너리 자료형 변수를 선언함

print(type(my_dict_01))

# dictionary_name = {key : value}   딕셔리의 구성  키와 밸류

my_info = {"name": "Boyeon", "age": 29, "location": "Seoul"}

my_info_01 = dict({"name": "Boyeon", "age": 29, "location": "Seoul"})

# fromkeys()

cities = ("Seoul", "Paris", "Madrid")

# fromkeys() 메서드를 통해서 'my_cities'라는 딕셔너리 생성하기

my_cities = dict.fromkeys(cities)  # 새로운 딕셔너리를 생성하는 메서드 파라미터로 2개 들어감. 하나일시 값은 null

print(my_cities)

# 딕셔너리의 모든 키에 동일한 값을 설정하는 다른 예

# 단일 값을 생성하기

city_type = "Capital"

my_cities = dict.fromkeys(cities, city_type)

print(my_cities)

# key에 set, list, dict같은 mutable 데이터는 할당 불가능!

# my_dictionary = {["Python"]: "languages"}
# print(my_dictionary)
# 출력된 결과
# line 1, in <module>
#    my_dictionary = {["Python"]: "languages"}

# TypeError: unhashable type: 'list'

# 한 딕셔너리 안에 같은 이름의 키는 한 개 이상 존재할 수 없다. 키는 고유하기 때문

# value는 중복이 가능

# len() : 파라미터로 전달된 객체의 총 길이를 반환하는 함수

print(len(my_info))

# return 3

# ---------------------------------------------------------
# ------------여기서부터 아주 중요함. ps자주 나옴------------------
# ---------------------------------------------------------

# items() : tuple형식의 key, value쌍을 모두 리턴

year_of_creation = {"Python": 1993, "JS": 1995, "HTML": 1993}

print(year_of_creation.items())  # 튜플 쌍으로 반환해줌

print(year_of_creation.keys())  # 키(들)를 리스트로 반환해줌

print(year_of_creation.values())  # 값들을 리스트로 반환해줌


# ---------------------------------------------------------
# ------------ 아주 중요.아주 중요.아주 중요.아주   ---------------
# ---------------------------------------------------------

# 딕셔너리의 특정 키-값에 접근하기

# 딕셔너리에서는 리스트와 완전히 동일한 방법을 사용할 수 없습니다.
# 딕셔너리는 키-값으로 이루어진 데이터 타입이기 때문에
# 인덱스 번호를 사용해 딕셔너리 내의 요소를 접근할 수 없기 때문입니다.

# 특정 키-값에 접근하는 기본 문법은 다음과 같다.

# dictionary_name[key]

# 그러니까, 인덱스로 접근하는 것이 아니라 키로 접근한다고 보면 된다

my_info = {"name": "Minho", "age": 30, "location": "Seoul"}
# 'age' 키에 할당된 값에 접근하기

print(my_info["age"])  # return 30

# 키가 존재하지 않으면, KeyError오류 발생

# search for the 'job' key

print("job" in my_info)

# get() : KeyError오류를 방지하려면 get()을 이용해서 접근하면 된다.

print(my_info.get("job"))

# 'job'이라는 key가 없기 때문에 None을 반환한다.  null반환 하는 것임. 없는것도 어떤 상태로 침. 그냥 dict[key]로 하면 에러 발생


# 딕셔너리 수정하기 .. 딕셔너리는  mutable이다~

# dictionary_name[key] = new_value

new_dict = {}

new_dict["name"] = "minwoo"

print(new_dict)

new_dict["name"] = "hwamin"

print(new_dict)

# 딕셔너리 병합하기 ->  update()

numbers = {"one": 1, "two": 2, "three": 3}
more_numbers = {"four": 4, "five": 5, "six": 6}

numbers.update(more_numbers)

print(numbers)


# 딕셔너리 삭제하기  ->  python의 대표적인 키워드 del     ,   cf  ..   pop()


my_information = {"name": "Boyeon", "age": 29, "location": "Seoul"}
del my_information["location"]
print(my_information)


my_information = {0: "Boyeon", 1: "samsung", 2: "Seoul"}

del my_information[1]

# delete key of samsung elmement

print(my_information)

my_information = {"Seoul": 0, "Paris": 100, "Madrid": 1010}

# pop()  :  키를 삭제를 하지만, 동시에 키에 할당된 값은 따로 저장하고 싶다면

score = my_information.pop("Paris")  # 여기서 return으로 100이 나옴 이것을 변수에 저장

print(score)

# 딕셔너리의 마지막 값만 제거하기 마치 스택의 pop()처럼 ..

# popitem()

my_information = {"name": "Boyeon", "age": 29, "location": "Seoul"}

my_information.popitem()
print(my_information)

my_information.popitem()
print(my_information)

my_information.popitem()
print(my_information)

# 딕셔너리 싹다 삭제하기   clear()


my_information = {"name": "Boyeon", "age": 29, "location": "Seoul"}

my_information.clear()

print(my_information)

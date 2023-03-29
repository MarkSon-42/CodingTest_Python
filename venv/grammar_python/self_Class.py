# 클래스의 사용 목적 : 변수와 함수를 묶어서 하나의 새로운 객체(타입)로 만드는 것

# 클래스를 정의한다는 것의 의미 : 새로운 데이터 타입을 정의한 것이다.

# 클래스를 실제로 사용하려면 인스턴스를 생성해야함.

class BusinessCard:

    # def __int__(self):
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr





card_001 = BusinessCard() # 정의된 클래스를 이용해서 인스턴스 생성하기 : 클래스 이름 뒤에 ()를 넣으면 된다.
print(card_001)







class Foo:
    def func_01():
        print("function 1")
    def func_02(self):
        print("function 2")

f = Foo()
print(f.func2())

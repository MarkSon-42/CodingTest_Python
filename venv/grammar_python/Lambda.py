# Python lambda Syntax:
# lambda arguments : expression


calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))

string = 'GeeksforGeeks'

# print(lambda string: string)

# 다양한 작업을 수행 하기위해 람다 반환 값 호출

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums() : ", filter_nums("Geeks101"))

do_exclaim = lambda s: s + "!"
print("do_exclaim():", do_exclaim("I am so fuxkin tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum(): ", find_sum(104051))

def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y

# 람다 함수와 def 키워드를 사용하여 정의된 다른 함수 의 주요 차이점은
# 람다 함수 내에서 여러 문을 사용할 수 없으며 허용되는 문도 람다 문 내에서 매우 제한된다는 것입니다.
# 람다 함수를 사용하여 복잡한 작업을 수행하면 코드의 가독성에 영향을 미칠 수 있습니다.


lambda_cube = lambda num: num ** 3

# call VS invoke

# 프로그래밍에서 "호출"과 "호출"은 둘 다 함수나 메서드를 실행하는 행위를 나타냅니다. 그러나 사용법에는 미묘한 차이가 있습니다.
#
#
# "호출"은 함수 또는 메서드의 실행을 나타내는 데 사용할 수 있는 보다 일반적인 용어입니다. 단순히 필요한 인수를 제공하여 함수나 메서드를 실행하는 것을 의미합니다.
#
#
# "Invoke"는 개체 지향 프로그래밍에서 자주 사용되는 보다 구체적인 용어입니다. 객체에서 메서드를 호출하는 행위를 말합니다. 개체에서 메서드를 호출하면 해당 특정 개체와 연결된 함수를 호출하는 것입니다.
#
#
# 요약하면 "호출"은 함수나 메서드의 실행을 나타내는 데 사용할 수 있는 일반적인 용어인 반면 "호출"은 개체 지향 프로그래밍에서 개체에 대한 메서드를 호출하는 것을 나타내는 보다 구체적인 용어입니다.
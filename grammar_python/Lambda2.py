# 람다 함수는 함수 내부에서 사용할 때 더 유용하다.

# 예를들면 sorted(), filter(), map()
ln = ["1", "2", "9", "0", "-1", "-2"]

print("Sorted numerically:",
      sorted(ln, key=lambda x: int(x)))

print(list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), ln)))

print(list(map(lambda x: str(int(x) + 10), ln)))


my_list = [1, 2, 3, 4, 5]

new_list = list(filter(lambda x: x % 2 != 0, my_list))

print(new_list)
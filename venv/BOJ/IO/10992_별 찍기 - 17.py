# 반복문 그리고 규칙성

n = int(input())
for i in range(1, n+1):
    if i == 1:
        print(' ' * (n - i) + "*")
    elif i == n:
        print("*" * ((2*n) - 1))
    else:
        print(' ' * (n - i) + "*" + ' ' * ((2*i) - 3) + "*")




# n = 4

 #
 #    *
 #   * *
 #  *   *
 # *******

 # fst  ->  n-1 ->' ' mid *
 # send ~ last - 1 ->
 # last -> *****... 2*n-1

 # c++ 처럼 2중 for로 짜는게 아니네..?
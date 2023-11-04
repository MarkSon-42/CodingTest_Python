# https://blog.naver.com/PostView.naver?blogId=wideeyed&logNo=221745416992

# sort()는  list.sort() 형식으로 "리스트형의 메소드"이며 리스트 원본값을 직접 수정한다.

# sorted()는 sorted(list) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고, 정렬 값을 반환한다.

a1 = [5, 8, 7 ,4, 9, 3]
print(a1)
a2 = a1.sort() # #원본을 정렬하고 수정합니다.
print("after sort()")
print(a1)
print(a2)


b1 = [7, 4, 8, 1, 9, 8, 7]
print(b1)
b2 = sorted(b1)
print("after sorted()")
print(b1)
print(b2)

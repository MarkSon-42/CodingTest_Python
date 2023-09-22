arr1 = [list(map(int,input().split())) for _ in range(3)]
input()  # 이거 개오반데.. 그래도 알아두자  입력을 뭐 이따위로..
arr2 = [list(map(int,input().split())) for _ in range(3)]


for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end = " ")
    print()
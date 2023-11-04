import numpy as np
def solution(arr1, arr2):
    anum = np.array(arr1)
    bnum = np.array(arr2)

    answer = anum.dot(bnum)

    answer = answer.tolist()
    return answer
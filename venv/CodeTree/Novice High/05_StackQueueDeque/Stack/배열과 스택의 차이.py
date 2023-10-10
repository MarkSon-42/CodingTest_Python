# function push(arr, E)
#   if arr.size == maxsize          // 배열에 이미 원소들이 가득 채워져 있다면,
#     throw exception()             // 에러 메세지를 던져줍니다.
#   arr.append(E)                   // 정상적인 상황이라면, E를
#                                   // 마지막 위치에 추가해줍니다.
#
# function pop(arr)
#   if arr.size == 0                // 배열에 아무런 원소도 없다면
#     throw exception()             // 에러 메세지를 던져줍니다.
#   set last = arr[arr.size - 1]    // 정상적인 상황이라면, 마지막 값을 변수에 저장해두고
#   delete arr[arr.size - 1]        // 맨 끝에 있는 값을 실제로 제거한 뒤
#   return last                     // 마지막에 있었던 값을 반환해줍니다.


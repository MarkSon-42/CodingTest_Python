# Example 1 : 배열이 있고 타겟넘버 찾기 _ 그냥 반복문 도는것 보다 시간복잡도가 더 좋다.
# TC = O(n)
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return True
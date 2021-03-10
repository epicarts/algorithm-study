# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution:
    def twoSum(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums): # O(n)
            nums_map[num] = i # 키와 인덱스를 딕셔너리로.

        for i, num in enumerate(nums):
            if target - num in nums_map: # O(1)  => 해시 테이블.
                if i != nums_map[target - num]: # 자기 자신은 제외해야함.
                    return [i, nums_map[target - num]] # 현재 인덱스와 맵에 인덱스르 조회


nums = [2,7,11,15]
target = 9
# output: [0,1]



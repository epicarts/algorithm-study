from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 투 포인터 사용을 위한 정렬
        results = []

        for i in range(len(nums) - 2): # i 값을 기준으로 0 인덱스 부터 탐색.
            if i > 0 and nums[i] == nums[i - 1]: # 중복된 값을 넘기기, i > 0 인 경우는 맨처음만 적용.
                continue
            left = i + 1 # i 다음부터 ~ 증가
            right = len(nums) - 1  # 맨 마지막 배열부터 ~ 감소
            while left < right: # index가 교체 되기 전까지
                sum = nums[i] + nums[left] + nums[right]

                # 0이 정답이 되도록 해야함.
                if sum < 0: # 값을 키워야 하므로 우측으로 이동
                    left += 1
                elif sum > 0: # 값을 줄여야 하므로 좌측으로 이동
                    right -= 1
                else: # 정답이 ㄴ경우
                    results.append([nums[i], nums[left], nums[right]])

                    # 바로 옆에 동일한 값이 있을 수 있으므로 중복 값 제거.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 중복값의 끝까지 찾았으므로, 그 다음으로 값을 하나 증가 시켜주어야함
                    left += 1
                    # right -= 1
        return results

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

print(Solution().threeSum(nums))

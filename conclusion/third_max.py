from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return nums[-3] if len(nums) > 2 else nums[-1]

nums = [-1,2,3]
s = Solution()
res = s.thirdMax(nums)
print(res)
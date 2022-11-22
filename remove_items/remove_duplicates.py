from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        print(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
s.removeDuplicates(nums)
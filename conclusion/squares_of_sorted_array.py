from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        lo, hi = 0, len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if (abs(nums[lo]) >= abs(nums[hi])):
                res.insert(0, nums[lo] * nums[lo])
                lo += 1
            else:
                res.insert(0, nums[hi] * nums[hi])
                hi -= 1
        return res

nums = [-7,-3,2,3,11]
r = Solution().sortedSquares(nums)
print(r)
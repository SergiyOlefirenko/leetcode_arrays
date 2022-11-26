'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            val = abs(nums[i])-1
            if nums[val] > 0:
                nums[val] = nums[val] * -1
            print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res


# best time:
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        missing = []
        s = set(nums)
        n = len(nums)
        for i in range(1,n+1):
            if i not in s:
                missing.append(i)
        return missing



nums = [4,3,2,7,8,2,3,1]
res = Solution().findDisappearedNumbers(nums)
print(res)

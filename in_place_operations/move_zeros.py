from typing import List


nums = [0,1,0,3,12]



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
                length -= 1
            i += 1

s = Solution()
s.moveZeroes(nums)
print(nums)
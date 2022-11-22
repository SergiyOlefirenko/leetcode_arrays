from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            print(f'i: {i}')
            if nums[i] == val:
                for j in range(i, len(nums)-1):
                    print(f'j: {j}')
                    nums[j] = nums[j+1]
                i -= 1
                nums.pop()
            i += 1
            print(nums)

    def removeElementBetter(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)



nums = [0,1,2,2,3,0,4,2]
val = 2
s = Solution()
s.removeElement(nums, val)
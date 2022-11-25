from typing import List


class Solution:
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #     i = 0
    #     length = len(nums)
    #     while i < length:
    #         if nums[i] % 2 != 0:
    #             nums.append(nums.pop(i))
    #             i -= 1
    #             length -= 1
    #         i += 1
    #     return nums

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pointer = 0
        index = 0
        for num in nums:
            if num % 2 == False:
                nums[pointer], nums[index] = num, nums[pointer]
                pointer += 1
            index += 1
        return nums

nums = [3,1,2,4]
s = Solution()
s.sortArrayByParity(nums)
print(nums)

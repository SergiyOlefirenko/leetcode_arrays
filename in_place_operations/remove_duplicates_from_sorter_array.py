from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums), nums
    

s = Solution()
arr = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(arr))
print(arr)
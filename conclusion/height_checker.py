from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        copy_arr = sorted(heights)
        for i in range(len(heights)):
            if copy_arr[i] != heights[i]:
                result += 1
        return result

s = Solution()
heights = [5,1,2,3,4]
res = s.heightChecker(heights)
print(res)
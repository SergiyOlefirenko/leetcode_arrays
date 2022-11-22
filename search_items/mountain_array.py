from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peakIndex = 0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]: peakIndex = i + 1
            else: break
        if peakIndex == 0 or peakIndex == len(arr)-1: return False
        for j in range(peakIndex, len(arr)-1):
            if arr[j] <= arr[j+1]: return False
        return True



arr = [1,1,1,1,1,1,1,2,1]
s = Solution()
print(s.validMountainArray(arr))
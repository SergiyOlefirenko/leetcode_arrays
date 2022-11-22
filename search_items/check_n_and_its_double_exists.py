from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2) != i:
                return True
        return False


arr = [10,2,5,3]
s = Solution()
print(s.checkIfExist(arr=arr))

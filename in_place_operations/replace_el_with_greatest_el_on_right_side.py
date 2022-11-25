from typing import List


arr = [17,18,5,4,6,1]
# arr = [0]

class Solution:
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     for i in range(len(arr)):
    #         print(f'i: {i}, arr[i]: {arr[i]}, max to right: {max(arr[i:])}')
    #         if i != len(arr)-1:
    #             arr[i] = max(arr[i+1:])
    #         else:
    #             arr[i] = -1
    #     print(arr)

    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     arr_length = len(arr)
    #     max_to_right = arr[arr_length-1]
    #     arr[arr_length-1] = -1
    #     for i in range(arr_length-2, -1, -1):
    #         if arr[i] < max_to_right:
    #             arr[i] = max_to_right
    #         else:
    #             max_to_right, arr[i] = arr[i], max_to_right
    #     return arr

    def replaceElements(self, arr: List[int]) -> List[int]:
        max_v = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > max_v:
                max_v, arr[i] = arr[i], max_v
            else:
                arr[i] = max_v
        arr[-1] = -1
        return arr

s = Solution()
s.replaceElements(arr)

print(arr)
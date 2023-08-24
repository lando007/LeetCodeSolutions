from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = 0
        while x <= len(nums) - 1 :

            if nums[x] == target:
                return x

            elif nums[x] >= target:
                y = x - 1
                return x
            else:
                x += 1
        return x
    test = [1,3,5,6]
    # 0 1 2 3 4 5
    removeValue = 7
    Solution = searchInsert(test, test, removeValue)
    print(Solution)

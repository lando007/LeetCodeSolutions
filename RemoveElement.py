from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        intIndex = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[intIndex] = nums[x]
                intIndex += 1
        return intIndex

    test = [0,1,2,2,3,0,4,2]
    removeValue = 2
    Solution = removeElement(test, test, removeValue)
    print(Solution)

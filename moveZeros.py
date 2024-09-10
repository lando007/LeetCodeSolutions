"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for x in nums:
            if (x == 0 and len(nums) == 1):
                exit
            elif x == 0:
                nums.remove(x);
                nums.append(0)
        return nums


nums = [0]

test = Solution().moveZeroes(nums)
print(test)

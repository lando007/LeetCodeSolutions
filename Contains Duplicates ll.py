"""Given an integer array nums and an integer k, return true if there are two
distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false"""

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = 0
        y = 0
        while x < len(nums):
            while y < len(nums):
                if nums[x] == nums[y] and x != y :
                    if abs(x - y) <= k:
                       return True

                y +=1
            x +=1
            y=0
        return False

nums = [1,0,1,1]
k = 1
test = Solution().containsNearbyDuplicate(nums, k)
print(test)

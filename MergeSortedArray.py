"""Given a string s, find the length of the longest
substring
 without repeating characters.Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x=0
        y = len(nums1) - 1
        a = 0
        endOfArray = n
        restOfNumbers=0
        if len(nums2) == 0:
            return nums1
        if m == 0:
            temp = len(nums1)
            while restOfNumbers < len(nums2):
                nums1.append(nums2[restOfNumbers])
                restOfNumbers +=1
            while temp > 0:
                nums1.remove(0)
                temp-=1
            return nums1
        while m > 0:
            nums1.remove(nums1[y])
            y-=1
            m-=1

        while n > 0:
            # if num1< num2
            if nums1[x] < nums2[a]:
                x+=1
                if x == endOfArray:
                    while restOfNumbers < len(nums2):

                        nums1.append(nums2[restOfNumbers])
                        restOfNumbers +=1
                        n-=1

            else:
                nums1.insert(x, nums2[a])
                removedValue  = nums2[0]
                nums2.remove(removedValue)

                x=0
                n-=1
        print(nums1)
        #move to next num1
        # else insert into nums1 from nums2







nums1 = [0,0,0,0,0]
m = 0
nums2 = [1,2,3,4,5]
n = 5
test = Solution().merge(nums1, m, nums2, n)
print(test)

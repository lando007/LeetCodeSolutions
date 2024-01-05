"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store."""

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
"""        y = 0
        currentHigh = 0
        count = 0
        currentX = 0
        for x in height:
            if x < y:
                currentX+=1
                continue
            else:
                for z in height:
                    if count == currentX:
                        count+=1
                        continue
                    else:
                        if x > z:
                            setHight = z
                        else:
                           setHight = x
                        if currentHigh > (z-count) * setHight:
                            count+=1
                            continue
                        else:
                            currentHigh = (z-count) * setHight
                            print(currentHigh)
                            print(count)
                            count+=1
            currentX+=1
            count = 0
        return  currentHigh"""


        y = height[0]
        current = 0
        count = 0
        xlocation = 0
        for x in height:
            if x-(count) > y:
                y = x

                xlocation = count
                count +=1
            else:
                if x < y:
                    height = x
                else:
                    height = y
                if height * (count-xlocation) > current:
                    current = (height * (count-xlocation))
                    count+=1

                else:
                    count+=1
                    continue
        return current




s = [1,8,6,2,5,4,8,3,7]
test = Solution().maxArea(s)
print(test)

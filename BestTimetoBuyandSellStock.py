"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0."""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestCount = prices[0]
        lowestNumber = prices[0]
        highestCount = 0
        highestNumber = 0
        if len(prices) == 1:
            return 0
        for count, x in enumerate(prices):
            if (count < lowestCount and x < lowestNumber) or (x == 0 and count != len(prices)-1 ):
                lowestCount = count
                lowestNumber = x
            if count > highestCount and x > highestNumber:
                highestCount = count
                highestNumber = x


        return highestNumber - lowestNumber

nums = [2,1,2,0,1]

test = Solution().maxProfit(nums)
print(test)

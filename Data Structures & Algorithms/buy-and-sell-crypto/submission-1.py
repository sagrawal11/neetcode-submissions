class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # let's first establish our counter variable for profits
        max_profit = 0

        left = 0
        right = 1

        while left < right and right < len(prices):
            print(left)
            print(right)
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            if prices[left] >= prices[right]:
                left = right
            right += 1
        return max_profit



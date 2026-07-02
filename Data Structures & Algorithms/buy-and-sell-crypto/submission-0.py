class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            diff = prices[i] - smallest
            if diff > max_profit:
                max_profit = diff
            if prices[i] < smallest:
                smallest = prices[i]
        
        return max_profit
        
        
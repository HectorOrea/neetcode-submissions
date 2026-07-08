class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        highest_price = 0
        most_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            highest_price = max(highest_price, prices[i]) # most price we can sell it for on or after day i
            p = highest_price - prices[i] # most we can profit if we bought today
            most_profit = max(most_profit, p)
        return most_profit

        
        
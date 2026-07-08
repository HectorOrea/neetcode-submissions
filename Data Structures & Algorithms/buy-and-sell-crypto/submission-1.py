class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can track the lowest price up to and including a day
        # we can track the biggest price after and including a given day
        # we can be aware of 0

        #     [10, 1, 5, 7, 6]
        # A = [10, 1, 1, 1, 1]
        # B = [10, 7, 7, 7, 6]

        # max (A[r] - A[l], 0) for r > l

        # let Z = max(A[i]) for i >= l

        # soln = max(Z(l) - A[l], 0)

        # we can compute Prof = Z(l) - A(l) in a single pass

        Z = [0 for _ in range(len(prices))] # Z[i] is most we can sell it for on or after day i
        profits = [0 for _ in range(len(prices))] # profits[i] is max profit if we buy on day i
        highest_price = 0
        most_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            highest_price = max(highest_price, prices[i])
            Z[i] = highest_price
            profits[i] = Z[i] - prices[i]
            most_profit = max(most_profit, profits[i])
        return most_profit

        
        
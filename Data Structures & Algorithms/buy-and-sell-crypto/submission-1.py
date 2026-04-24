class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] --> the price of neet coin on that day 

        # choose a single coin and sell on that different day 

        lowest_price = prices[0]
        maximum_profit = 0 

        for i in range(1,len(prices)):
            lowest_price = min(lowest_price, prices[i])
            maximum_profit = max(maximum_profit, prices[i]-lowest_price)

        return maximum_profit


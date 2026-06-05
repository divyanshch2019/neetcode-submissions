class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) ==0 : result
        buy_price = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-buy_price
            if profit < 0:
                buy_price = prices[i]
                continue
            result = max(result,profit)
        return result
        
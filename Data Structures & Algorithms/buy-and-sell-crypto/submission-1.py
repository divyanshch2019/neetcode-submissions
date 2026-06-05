class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result =0
        if not prices or len(prices)<2: return result
        prev_price = prices[0]
        for i in range(1, len(prices)):
            running_profit= prices[i] - prev_price
            if running_profit >0:
                result = max(result,running_profit)
            else:
                #reset the prev_price
                prev_price = prices[i]
        return result
        
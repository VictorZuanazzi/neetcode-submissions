class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # # naive:
        # max_profit = 0
        # for i, buy in enumerate(prices[:-1]):
        #     sell = max(prices[i + 1:])
        #     max_profit = max(max_profit, sell - buy)

        
        max_profit = 0
        idx_buy = 0
        idx_sell = len(prices) - 1 
        for i, p in enumerate(prices[:-1]):
            if p < prices[idx_buy]:
                price_buy = p
                idx_buy = i

            profit_buy = prices[idx_sell] - p
            profit_sell = p - prices[idx_buy]
            
            max_profit = max(max_profit, profit_buy, profit_sell)
        
        return max_profit


        
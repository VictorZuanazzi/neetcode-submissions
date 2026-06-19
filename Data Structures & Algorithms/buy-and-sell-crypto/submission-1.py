class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # # naive:
        # max_profit = 0
        # for i, buy in enumerate(prices[:-1]):
        #     sell = max(prices[i + 1:])
        #     max_profit = max(max_profit, sell - buy)

        # # My answer!
        # max_profit = 0
        # idx_buy = 0
        # idx_sell = len(prices) - 1 
        # for i, p in enumerate(prices[:-1]):
        #     if p < prices[idx_buy]:
        #         idx_buy = i

        #     profit_buy = prices[idx_sell] - p
        #     profit_sell = p - prices[idx_buy]
            
        #     max_profit = max(max_profit, profit_buy, profit_sell)

        # Two pointers:
        idx_buy = 0
        idx_sell = 1
        max_profit = 0
        while idx_sell < len(prices):
            sell_price = prices[idx_sell]
            buy_price = prices[idx_buy]

            if sell_price < buy_price:
                idx_buy = idx_sell
                idx_sell += 1
                continue

            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)
            
            idx_sell += 1
        
        return max_profit


        
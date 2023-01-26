def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0

        for sell in range(len(prices)):
            if prices[sell] <= prices[buy]:
                buy = sell
            profit = max(profit, prices[sell] - prices[buy])
        
        return profit
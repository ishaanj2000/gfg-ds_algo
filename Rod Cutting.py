      def cutRod(self, price, n):
        memo ={}
        def maximumProfit(prices, n, memo):
            if n == 0:
                return n
            if n in memo:return memo[n]
            maxProfit = -999999
            for i in range(1, n + 1):
                maxProfit = max(maxProfit, prices[i - 1] + maximumProfit(prices, n - i, memo))
            
            memo[n] = maxProfit
            return memo[n]
            
        
        return maximumProfit(price, n, memo)

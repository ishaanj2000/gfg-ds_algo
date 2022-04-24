      def minSum(arr, n):
        
        
        if n <= 4:
            return min(arr)
            
        
        dp = {}
        
        for i in range(0,4):
            dp[i] = arr[i]
            
        for i in range(4, n):
            dp[i] = arr[i] + min(dp[i-4],dp[i-3], dp[i-2], dp[i-1])
            
        
        return min(dp[n-4], dp[n-3], dp[n-2], dp[n-1])    

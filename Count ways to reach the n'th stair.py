      def countWays(self,n):
        dp={}
        def count(n, dp):
            
            if n == 1 or n == 0:
                return 1
            
            
            if n in dp:
                return dp[n]
            
            dp[n] = (count(n-1, dp) + count(n-2, dp))%1000000007
            
            return dp[n]
        return count(n, dp)
    

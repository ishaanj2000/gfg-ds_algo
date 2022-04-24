      def count(self, S, m, n): 
        dp = {}
        def change(S, m, n):
            if n == 0:
                dp[(m,n)] = 1
                return 1
            if (n < 0):
                dp[(m,n)] = 0
                return 0
 
    
            if (m <=0 and n >= 1):
                dp[(m,n)] = 0
                return 0
                
            if(m,n) in dp:
                return dp[(m,n)]
                
            incl = change(S, m, n-S[m-1])
            dp[(m,n)] = change(S, m, n-S[m-1])
            excl = change(S, m-1, n)
            dp[(m,n)] = change(S, m-1, n)
            
            dp[(m,n)] = incl + excl
                
            return dp[(m,n)]
        
        return change(S,m ,n)

      def countDistinct(self, A, N, K):
        d = defaultdict(lambda:0)
        dist = 0
        arr = []
        
        for i in range(K):
            
            if d[A[i]] == 0:
                
                dist+=1
            
            d[A[i]]+=1
        
        arr.append(dist)
        
        for i in range(K, n):
            
            if d[A[i-K]] == 1:
                dist-=1
            
            d[A[i-K]] -=1
            
            
            if d[A[i]] == 0:
                dist+=1
            d[A[i]] +=1
            
            
            arr.append(dist) 
            
        return arr

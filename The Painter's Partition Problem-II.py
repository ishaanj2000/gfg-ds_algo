'''Dilpreet wants to paint his dog's home that has n boards with different lengths.
The length of ith board is given by arr[i] where arr[] is an array of n integers. 
He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board. 

The problem is to find the minimum time to get this job done if all painters start together 
with the constraint that any painter will only paint continuous boards, 
say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.'''

      def isvalid(self,arr, n, k , mx):
        
        n_students = 1
        s = 0
        
        for i in range(n):
            s += arr[i]
            
            if s > mx:
                n_students+=1
                s = arr[i]
            
            if n_students > k:
                return False
        
        return True
      
      
      def minTime (self, arr, n, k):
        
        
        start = max(arr)
        end = sum(arr)
        res = -1
        
        while start <= end:
            mid = (start + (end - start)//2)
            
            if self.isvalid(arr, n, k, mid) == True:
                res = mid
                end = mid-1
            
            else:
                start = mid + 1
            
        return res

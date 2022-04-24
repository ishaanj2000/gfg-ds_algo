''' Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
The efficient way is the one that involves the least number of multiplications.

The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) 
where the ith matrix has the dimensions (arr[i-1] x arr[i]).'''

      def matrixMultiplication(self, N, arr):
        dp ={}
        def mcm(arr, i, j, dp):
            
            if i>j or i == j: return 0
            
            
            mini = sys.maxsize
            
            if (i,j) not in dp: 
            
                for k in range(i, j):
                    
                    temp = (mcm(arr, i, k, dp) + mcm(arr, k+1, j, dp) + arr[i-1] * arr[k] * arr[j])
                    
                    if temp < mini:
                        mini = temp
                        
                dp[(i, j)] = mini
            return dp[(i,j)]
            
        return mcm(arr, 1, N-1, dp)

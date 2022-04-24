'''Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].

Matrix [r+1] [c]
Matrix [r+1] [c-1]
Matrix [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to row N-1.'''
      
      
      
      def maximumPath(self, N, Matrix):
        # code here
        
        arr = [[0 for i in range(N)] for i in range(N)]
        
        for i in range(1):
            for j in range(N):
                arr[i][j] = Matrix[i][j]
                
        
        for i in range(1, N):
            for j in range(N):
                ans = 0
                
                if j != 0 and j!= N-1:
                    ans = max(arr[i-1][j], arr[i-1][j+1], arr[i-1][j-1]) + Matrix[i][j]
                    arr[i][j] = ans
                
                elif j == 0:
                    ans = max(arr[i-1][j], arr[i-1][j+1]) + Matrix[i][j]
                    arr[i][j] = ans
                
                elif j == N-1:
                    ans = max(arr[i-1][j], arr[i-1][j-1]) + Matrix[i][j]
                    arr[i][j] = ans
        
        mx = 0      
        for i in range(N):
            for j in range(N):
                if arr[i][j] > mx:
                    mx = arr[i][j]
        return mx

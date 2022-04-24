def check(self,A,B,N):
        
        A.sort()
        B.sort()
        a =0
        
        for i in range(len(A)):
            if A[i] != B[i]:
                a = 1
                break
            else: a = 0
        
        if a == 0:
          return True 
        
        else:
          return False

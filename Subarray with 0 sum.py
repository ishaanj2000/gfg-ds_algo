def subArrayExists(self,arr,n):
        
        s = set()
        cs = 0
        
        for i in arr:
            
            cs+=i
            
            if cs in s or cs == 0:
                return True
            s.add(cs)
        return False

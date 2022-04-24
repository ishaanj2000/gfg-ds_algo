    def max_of_subarrays(self,arr,n,k):
        
        j = 0
        m = max(arr[:k])
        ans = [m]
        
        for i in range(k,n):
            if m!=arr[i-k]:
                m=max(m,arr[i])
            else:
                m=max(arr[i-k+1:i+1])
            ans.append(m)
        return ans
        

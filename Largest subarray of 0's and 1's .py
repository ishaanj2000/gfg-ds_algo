def maxLen(self,arr, N):
        hash_map = defaultdict(lambda:0) 
        curr_sum = 0
        max_len = 0
      
        for i in range (0, N):
            if(arr[i] == 0):
                arr[i] = -1
            else:
                arr[i] = 1

        for i in range (0, N):
            curr_sum = curr_sum + arr[i]
            if (curr_sum == 0):
                max_len = i + 1
            if curr_sum in hash_map:
    
                if max_len < i - hash_map[curr_sum]:
                    max_len = i - hash_map[curr_sum]
                    
            else:
                hash_map[curr_sum] = i 
     
        return max_len

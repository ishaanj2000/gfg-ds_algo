def zigZag(self,arr, n):
		
		flag = True # '<'
		for i in range(n-1):
		    if flag == True:
    		    	if arr[i] > arr[i+1]:
    		        	arr[i], arr[i+1] = arr[i+1], arr[i]
		    else: # '>'
		        if arr[i]<arr[i+1]:
		            arr[i], arr[i+1] = arr[i+1], arr[i]
		            
		    flag = bool(1-flag)
        return arr

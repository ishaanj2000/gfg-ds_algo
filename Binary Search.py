def binarysearch(self, arr, n, k):
		
		
		high = n-1
		low = 0
		
		
		while high >=low:
		    
            mid = low + (high - low) // 2
		    if k == arr[mid]:
		        return mid 
		        
		    elif k > arr[mid]:
		        
		        low = mid+1
		        
		    elif k < arr[mid]:
		        high = mid-1
		        
		       
		        
		return -1

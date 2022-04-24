  def maxSubstring(self, S):
		
		m = 0
		s = 0
		c =0
		for i in S:
		    if i == '1':
		        s -=1
		        c+=1
		    else:
		        s+=1
		    
		    if s<0:
		        s= 0
		        
		    if c == len(S):
		        return -1
		        
		    
		        
		    m = max(s, m)
	    return m

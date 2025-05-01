#User function Template for python3

class Solution:
	def singleNum(self, arr):
	    xor=0
		for num in arr:
		    xor^=num
		    
		xor&=-xor
		result=[0,0]
		
		for num in arr:
		    if (num&xor)==0:
		        result[0]^=num
		        
		    else:
		        result[1]^=num
		        
        if result[0]>result[1]:
            result[0],result[1]=result[1],result[0]
            
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
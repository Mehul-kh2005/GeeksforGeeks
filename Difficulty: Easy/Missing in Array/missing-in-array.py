class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        XOR1=0
        XOR2=0
        
        for i in range(n-1):
            XOR1^=arr[i]
            
        for i in range(1,n+1):
            XOR2^=i
            
        return XOR1^XOR2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends
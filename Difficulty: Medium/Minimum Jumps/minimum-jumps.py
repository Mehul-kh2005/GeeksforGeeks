class Solution:
	def minJumps(self, arr):
	    n = len(arr)

    
        dp = [float('inf')] * n
        dp[n - 1] = 0
    
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + arr[i] + 1, n)):
                if dp[j] != float('inf'):
                    dp[i] = min(dp[i], 1 + dp[j])
    
        if dp[0] == float('inf'):
            return -1
    
        return dp[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends
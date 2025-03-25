class Solution:
	def minCoins(self, coins, sum):
		dp = [float('inf')] * (sum + 1)
    
        dp[0] = 0 
        
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, sum + 1):
                
                take = float('inf')  
                noTake = float('inf') 
                
                if j - coins[i] >= 0 and coins[i] > 0:
                    take = dp[j - coins[i]]
                    
                    if take != float('inf'): 
                        take += 1
                
                if i + 1 < len(coins):
                    noTake = dp[j] 
                    
                dp[j] = min(take, noTake)
        
        return dp[sum] if dp[sum] != float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends
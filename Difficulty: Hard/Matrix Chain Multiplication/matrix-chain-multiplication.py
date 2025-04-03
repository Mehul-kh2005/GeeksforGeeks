class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)

        dp = [[0] * n for _ in range(n)]
    
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
    
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)
    
        return dp[0][n - 1]
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends
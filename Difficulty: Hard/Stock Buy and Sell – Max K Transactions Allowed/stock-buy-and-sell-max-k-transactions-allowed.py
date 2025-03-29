class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
    
        curr = [[0] * 2 for _ in range(k+1)]
        next = [[0] * 2 for _ in range(k+1)]
    
        for i in range(n-1, -1, -1):
            for l in range(1, k+1):
              
                curr[l][1] = max(-prices[i] + next[l][0], next[l][1])
                
                curr[l][0] = max(prices[i] + next[l-1][1], next[l][0])
                
            next = [row[:] for row in curr]
        
        return curr[k][1] 

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends
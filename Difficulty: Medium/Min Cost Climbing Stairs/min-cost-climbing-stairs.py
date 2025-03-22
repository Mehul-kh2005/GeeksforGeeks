#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        
        prev2=cost[0]
        prev1=cost[1]
        
        for i in range(2,n):
            curr=cost[i]+min(prev2,prev1)
            prev2=prev1
            prev1=curr
            
        return min(prev1,prev2)

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends
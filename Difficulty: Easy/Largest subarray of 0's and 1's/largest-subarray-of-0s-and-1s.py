class Solution:
    def maxLen(self, arr):
        mp={}
        prefix_sum=0
        result=0
        
        for i in range(len(arr)):
            prefix_sum+=-1 if arr[i]==0 else 1
            
            if prefix_sum==0:
                result=i+1
                
            if prefix_sum in mp:
                result=max(result,i-mp[prefix_sum])
                
            else:
                mp[prefix_sum]=i
                
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends
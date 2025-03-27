class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        prev = [False] * (sum + 1)
        curr = [False] * (sum + 1)
    
        prev[0] = True
    
        for i in range(1, n + 1):
            for j in range(sum + 1):
                if j < arr[i - 1]:
                    curr[j] = prev[j]
                else:
                    curr[j] = prev[j] or prev[j - arr[i - 1]]
            prev = curr.copy() 
    
        return prev[sum]
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
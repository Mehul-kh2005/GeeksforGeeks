#User function Template for python3

class Solution:
    def getMinDiff(self,arr,k):
        arr.sort()
        diff = arr[-1] - arr[0]
        
        for i in range(len(arr) - 1):
            lower = min(arr[0] + k, arr[i + 1] - k)
            upper = max(arr[-1] - k, arr[i] + k)
            diff = min(diff, upper - lower)
        
        return diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        solution = Solution()
        res = solution.getMinDiff(arr, k)
        print(res)
        print("~")

# } Driver Code Ends
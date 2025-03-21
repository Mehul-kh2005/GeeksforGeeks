
class Solution:
    def maxOfMins(self,arr):
        n = len(arr)
        res = [0] * n
        s = []
    
        lenArr = [0] * n
        
        for i in range(n):
            while s and arr[s[-1]] >= arr[i]:
                top = s.pop()
                windowSize = i if not s else i - s[-1] - 1
                lenArr[top] = windowSize
            s.append(i)
    
    
        while s:
            top = s.pop()
            windowSize = n if not s else n - s[-1] - 1
            lenArr[top] = windowSize
    
        for i in range(n):
            windowSize = lenArr[i] - 1  
            res[windowSize] = max(res[windowSize], arr[i])
    
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i], res[i + 1])
    
        return res

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends
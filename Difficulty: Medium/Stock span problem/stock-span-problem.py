#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def calculateSpan(self, arr):
        stack=[]
        result=[1]*len(arr)
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
                
            if not stack:
                result[i]=i+1
            else:
                result[i]=i-stack[-1]
                
            stack.append(i)
            
        return result

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends
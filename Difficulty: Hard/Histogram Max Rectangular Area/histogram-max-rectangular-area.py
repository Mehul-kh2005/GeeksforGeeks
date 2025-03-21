#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def getMaxArea(self,arr):
        n=len(arr)
        s=[]
        res=0
        
        for i in range(n):
            while s and arr[s[-1]]>=arr[i]:
                tp=s.pop()
                width=i if not s else i-s[-1]-1
                res=max(res,arr[tp]*width)
            
            s.append(i)
            
        while s:
            tp=s.pop()
            width=n if not s else n-s[-1]-1
            res=max(res,arr[tp]*width)
            
        return res


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends
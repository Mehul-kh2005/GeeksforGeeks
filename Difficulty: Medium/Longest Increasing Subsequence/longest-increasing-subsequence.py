class Solution:
    def lis(self, arr):
        n=len(arr)
        result=[1]*n
        
        for i in range(1,n):
            for prev in range(0,i):
                if arr[i]>arr[prev]:
                    result[i]=max(result[i],result[prev]+1)
                    
       
        return max(result)

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends
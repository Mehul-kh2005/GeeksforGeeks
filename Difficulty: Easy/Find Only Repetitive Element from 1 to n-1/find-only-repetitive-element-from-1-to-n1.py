#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        n=len(arr)
        total=sum(arr)
        
        return total-((n*(n-1))//2)
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends
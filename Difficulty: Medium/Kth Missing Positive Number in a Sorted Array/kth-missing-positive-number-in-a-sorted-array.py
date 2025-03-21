#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        count=0
        value=1
        set_elements=set(arr)
        
        while count!=k:
            if value not in set_elements:
                count+=1
            if count==k:
                return value
            value+=1
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
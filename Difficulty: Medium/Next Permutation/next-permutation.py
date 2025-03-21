#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        
        def swap(i,j):
            arr[i],arr[j]=arr[j],arr[i]
            
        def reverse(i):
            j=len(arr)-1
            
            while i<j:
                swap(i,j)
                i+=1
                j-=1
                
        i=len(arr)-2
        while arr[i+1]<=arr[i]:
            i-=1
            
        if i>=0:
            j=len(arr)-1
            
            while arr[j]<=arr[i]:
                j-=1
                
            swap(i,j)
            
        reverse(i+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
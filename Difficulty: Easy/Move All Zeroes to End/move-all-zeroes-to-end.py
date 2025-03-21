#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        n=len(arr)
        temp=[0]*n
        
        j=0
        for i in range(n):
            if arr[i]!=0:
                temp[j]=arr[i]
                j+=1
                
        for i in range(n):
            arr[i]=temp[i]
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends
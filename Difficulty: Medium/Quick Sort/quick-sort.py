#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low>=high:
            return
        
        pIndex=self.partition(arr,low,high)
        self.quickSort(arr,low,pIndex-1)
        self.quickSort(arr,pIndex+1,high)
        
        return arr
    
    def partition(self,arr,low,high):
        pivot=arr[low]
        i=low+1
        j=high
        
        while True:
            while i<=j and arr[i]<=pivot:
                i+=1
                
            while i<=j and arr[j]>pivot:
                j-=1
                
            if i<=j:
                arr[i],arr[j]=arr[j],arr[i]
                
            else:
                break
            
        arr[low],arr[j]=arr[j],arr[low]
        
        return j

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().split()))
        n = len(arr)
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        print("~")

# } Driver Code Ends
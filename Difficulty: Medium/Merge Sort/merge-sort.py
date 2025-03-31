#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    
    def merge(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
                
            else:
                temp.append(arr[right])
                right+=1
                
        while left<=mid:
            temp.append(arr[left])
            left+=1
                
        while right<=high:
            temp.append(arr[right])
            right+=1
                
        for i in range(low,high+1):
            arr[i]=temp[i-low]
            
    
    def mergeSort(self,arr, l, r):
        if l>=r:
            return 
        
        mid=(l+r)//2
        
        # Merge Sort for left Half
        self.mergeSort(arr,l,mid)
        
        # Merge Sort for Right Half
        self.mergeSort(arr,mid+1,r)
        
        # Merge both the arrays
        self.merge(arr,l,mid,r)
        
        return arr


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends
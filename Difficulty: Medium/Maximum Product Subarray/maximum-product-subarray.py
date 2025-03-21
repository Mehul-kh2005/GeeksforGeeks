#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        current_max=current_min=max_product=arr[0]
        
        for i in range(1,len(arr)):
            temp_max=current_max
            current_max=max(arr[i],temp_max*arr[i],current_min*arr[i])
            current_min=min(arr[i],temp_max*arr[i],current_min*arr[i])
            
            max_product=max(max_product,current_max)
            
        return max_product

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
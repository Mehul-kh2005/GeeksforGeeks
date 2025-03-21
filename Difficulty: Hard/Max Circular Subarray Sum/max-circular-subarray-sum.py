#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    current_max=global_max=arr[0]
    
    for i in range(1,len(arr)):
        current_max=max(arr[i],current_max+arr[i])
        global_max=max(global_max,current_max)
        
    current_min=global_min=arr[0]
    
    for i in range(1,len(arr)):
        current_min=min(arr[i],current_min+arr[i])
        global_min=min(global_min,current_min)
        
    total_sum=sum(arr)
    
    if global_max<=0:
        return global_max
    
    return max(global_max,total_sum-global_min)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends
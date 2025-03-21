#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        max_current=max_global=arr[0]
        
        for i in range(1,len(arr)):
            max_current=max(arr[i],max_current+arr[i])
            max_global=max(max_global,max_current)
            
        return max_global

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
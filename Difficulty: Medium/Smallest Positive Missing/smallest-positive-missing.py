#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        n = len(arr)
        
        # Step 1: Place each positive number at its correct index (if possible).
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                # Swap arr[i] with the element at its target position
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        # Step 2: Find the first missing positive integer.
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # If all numbers are present, the missing number is n + 1
        return n + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
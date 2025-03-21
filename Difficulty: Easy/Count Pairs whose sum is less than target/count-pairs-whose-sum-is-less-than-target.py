#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

#User function Template for python3
class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Sort the array to use two-pointer technique
        arr.sort()
        n = len(arr)
        count = 0
        
        # Two pointers: one starting at the beginning, one at the end
        left, right = 0, n - 1
        
        while left < right:
            # Calculate the sum of the two pointers
            current_sum = arr[left] + arr[right]
            
            if current_sum < target:
                # All pairs from left to right-1 are valid
                count += (right - left)
                left += 1  # Move left pointer forward
            else:
                right -= 1  # Move right pointer backward if sum >= target
        
        return count
        




#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
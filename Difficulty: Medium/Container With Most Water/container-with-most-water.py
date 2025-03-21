
class Solution:
    def maxWater(self, arr):
        n=len(arr)
        left,right=0,n-1
        result=0
        
        while left<right:
            water=min(arr[left],arr[right])*(right-left)
            result=max(result,water)
            
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
                
        return result

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
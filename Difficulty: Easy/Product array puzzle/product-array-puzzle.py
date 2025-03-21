#User function Template for python3
from math import prod

class Solution:
    def productExceptSelf(self, arr):
        total_product=1
        zero_count=0
        n=len(arr)
        
        for num in arr:
            if num==0:
                zero_count+=1
            else:
                total_product*=num
                
        result=[]
        for num in arr:
            if zero_count>1:
                result.append(0)
            elif zero_count==1:
                result.append(total_product if num==0 else 0)
            else:
                result.append(total_product//num)
                
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
class Solution:
    def maxValue(self, arr):
        
        def maxValueHelper(arr):
            dp=[0]*len(arr)
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            
            for i in range(2,len(arr)):
                dp[i]=max(dp[i-1],arr[i]+dp[i-2])
                
            return dp[-1]
            
        
        maxValue1=maxValueHelper(arr[:-1])
        maxValue2=maxValueHelper(arr[1:])
        
        return max(maxValue1,maxValue2)

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends
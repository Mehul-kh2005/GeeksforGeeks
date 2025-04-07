class Solution:
    def activitySelection(self, start, finish):
        ans=0
        arr=[]
        
        for i in range(len(start)):
            arr.append((finish[i],start[i]))
            
        arr.sort()
        finish_time=-1
        
        for i in range(len(arr)):
            activity=arr[i]
            if activity[1]>finish_time:
                finish_time=activity[0]
                ans+=1
                
        return ans

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
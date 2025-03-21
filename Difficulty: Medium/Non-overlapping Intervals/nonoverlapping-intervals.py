#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        intervals.sort(key=lambda x: x[1])
        
        count_removals = 0
        prev_end = float('-inf')  
        
        for start, end in intervals:
            if start < prev_end:  
                count_removals += 1
            else:  
                prev_end = end
        
        return count_removals
        



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends
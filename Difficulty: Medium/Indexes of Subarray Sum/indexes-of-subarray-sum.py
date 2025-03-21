#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        s, e = 0, 0
        res = []
    
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
    
            # If current sum becomes more or equal,
            # set end and try adjusting start
            if curr >= target:
                e = i
    
                # While current sum is greater, 
                # remove starting elements of current window
                while curr > target and s < e:
                    curr -= arr[s]
                    s += 1
    
                # If we found a subarray
                if curr == target:
                    res.append(s + 1)
                    res.append(e + 1)
                    return res
    
        # If no subarray is found
        return [-1]
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
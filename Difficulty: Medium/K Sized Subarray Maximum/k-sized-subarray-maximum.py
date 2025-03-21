from collections import deque
class Solution:
    def maxOfSubarrays(self,arr, k):
        n = len(arr)
    
        res = []
        dq = deque()
    
        for i in range(0, k):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
                
            dq.append(i)
    
        for i in range(k, len(arr)):
            res.append(arr[dq[0]])
    
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
    
            dq.append(i)
    
        res.append(arr[dq[0]])
    
        return res
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends
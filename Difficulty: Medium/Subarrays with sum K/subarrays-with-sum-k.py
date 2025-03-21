#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        cumulative_sum_count={0:1}
        cumulative_sum=0
        count=0
        
        for num in arr:
            cumulative_sum+=num
            
            if cumulative_sum-k in cumulative_sum_count:
                count+=cumulative_sum_count[cumulative_sum-k]
                
            cumulative_sum_count[cumulative_sum]=cumulative_sum_count.get(cumulative_sum,0)+1
            
        return count

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
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends
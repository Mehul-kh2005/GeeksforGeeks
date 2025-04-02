#User function Template for python3
class Solution:
	def countWays(self, digits):
		n = len(digits)

        if n == 0 or digits[0] == '0':
            return 0
    
        prev1, prev2 = 1, 0
    
        for i in range(1, n + 1):
            current = 0
            if digits[i - 1] != '0':
                current += prev1
            if i > 1:
                two_digit = (int(digits[i - 2]) * 10 + int(digits[i - 1]))
                if 10 <= two_digit <= 26:
                    current += prev2
    
            prev2 = prev1
            prev1 = current
        return prev1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends
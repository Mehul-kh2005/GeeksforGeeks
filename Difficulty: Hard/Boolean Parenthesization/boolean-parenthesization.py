#User function Template for python3
class Solution:
    def evaluate(self, b1, b2, op):
        if op == '&':
            return b1 & b2
        if op == '|':
            return b1 | b2
        return b1 ^ b2
    
    
    def countWays(self, s):
        n = len(s)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    
        # Base case: Single operands (T or F)
        for i in range(0, n, 2):
            dp[i][i][1] = 1 if s[i] == 'T' else 0
            dp[i][i][0] = 1 if s[i] == 'F' else 0
    
        # Iterate over different substring lengths
        for length in range(2, n, 2):  # length increases by 2 (odd indices are operators)
            for i in range(0, n - length, 2):
                j = i + length
                # Reset values for the current subproblem
                dp[i][j][0] = dp[i][j][1] = 0
    
                for k in range(i + 1, j, 2):  # Iterate over operators
                    op = s[k]
                    leftTrue, leftFalse = dp[i][k - 1][1], dp[i][k - 1][0]
                    rightTrue, rightFalse = dp[k + 1][j][1], dp[k + 1][j][0]
    
                    # Count ways to get True or False
                    if self.evaluate(1, 1, op):
                        dp[i][j][1] += leftTrue * rightTrue
                    if self.evaluate(1, 0, op):
                        dp[i][j][1] += leftTrue * rightFalse
                    if self.evaluate(0, 1, op):
                        dp[i][j][1] += leftFalse * rightTrue
                    if self.evaluate(0, 0, op):
                        dp[i][j][1] += leftFalse * rightFalse
    
                    if not self.evaluate(1, 1, op):
                        dp[i][j][0] += leftTrue * rightTrue
                    if not self.evaluate(1, 0, op):
                        dp[i][j][0] += leftTrue * rightFalse
                    if not self.evaluate(0, 1, op):
                        dp[i][j][0] += leftFalse * rightTrue
                    if not self.evaluate(0, 0, op):
                        dp[i][j][0] += leftFalse * rightFalse
    
        return dp[0][n - 1][1] 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends
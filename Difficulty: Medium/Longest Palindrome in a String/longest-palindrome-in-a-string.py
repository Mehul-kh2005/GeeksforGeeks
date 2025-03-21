
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        start, maxLen = 0, 1
    
        for i in range(n):
            dp[i][i] = True
    
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if maxLen < 2:
                    start = i
                    maxLen = 2
    
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
    
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
    
                    if k > maxLen:
                        start = i
                        maxLen = k
    
        return s[start:start + maxLen]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends
#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        n = len(s)

        curr = [0] * n
        prev = [0] * n
    
        for i in range(n - 1, -1, -1):
            curr[i] = 1
    
            for j in range(i + 1, n):
    
                if s[i] == s[j]:
    
                    curr[j] = prev[j - 1] + 2
                else:
                    curr[j] = max(prev[j], curr[j - 1])
    
            prev = curr[:]
    
        return curr[n - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
        print("~")
# } Driver Code Ends
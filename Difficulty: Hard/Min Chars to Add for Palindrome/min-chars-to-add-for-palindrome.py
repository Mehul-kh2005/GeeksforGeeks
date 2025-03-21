class Solution:
    def minChar(self, s):
        reversed_s = s[::-1]
        combined = s + '#' + reversed_s
        lps = self.computeLPS(combined)
        return len(s) - lps[-1]

    def computeLPS(self, pattern):
        lps = [0] * len(pattern)
        length = 0  
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
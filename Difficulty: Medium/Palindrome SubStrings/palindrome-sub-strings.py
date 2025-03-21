#User function Template for python3

class Solution:

    def countPS(self, s):
        n = len(s)
        count = 0
    
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
    
        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
    
        return count
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends
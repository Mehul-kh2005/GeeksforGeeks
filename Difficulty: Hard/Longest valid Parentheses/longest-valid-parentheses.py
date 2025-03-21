class Solution:
    def maxLength(self, s):
        open=close=0
        max_len=0
        
        for ch in s:
            if ch=="(":
                open+=1
            elif ch==")":
                close+=1
            if open==close:
                max_len=max(max_len,2*close)
            elif close>open:
                open=close=0
        
        open=close=0
        
        for ch in reversed(s):
            if ch=="(":
                open+=1
            elif ch==")":
                close+=1
            if open==close:
                max_len=max(max_len,2*open)
            elif open>close:
                open=close=0
                
        return max_len

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        char_index={}
        longest_substring=0
        start=0
        
        for end,char in enumerate(s):
            if char in char_index and char_index[char]>=start:
                start=char_index[char]+1
                
            char_index[char]=end
            
            longest_substring=max(longest_substring,end-start+1)
            
        return longest_substring

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
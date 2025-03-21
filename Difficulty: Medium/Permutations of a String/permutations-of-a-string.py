#User function Template for python3

class Solution:
    def findPermutation(self, s):
        def backtrack(path, used, res):
            if len(path) == len(s):
                res.add("".join(path)) 
                return

            for i in range(len(s)):
                if used[i]:  
                    continue

                used[i] = True
                path.append(s[i])
                backtrack(path, used, res)
                path.pop() 
                used[i] = False

        res = set()  
        used = [False] * len(s)
        backtrack([], used, res)

        return list(res)
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
class Solution:
	def editDistance(self, s1, s2):
		m = len(s1)
        n = len(s2)
    
        prev = 0
        curr = [0] * (n + 1)
    
        for j in range(n + 1):
            curr[j] = j
    
        for i in range(1, m + 1):
            prev = curr[0]
            curr[0] = i
            for j in range(1, n + 1):
                temp = curr[j]
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev
                else:
                    curr[j] = 1 + min(curr[j - 1], prev, curr[j])
                prev = temp
    
        return curr[n]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends
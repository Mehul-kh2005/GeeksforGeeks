
class Solution:
    def decodedString(self, s):
        res = ""
  
        for i in range(len(s)):
    
            if s[i] != ']':
                res += s[i]
    
            else:
              
                temp = ""
                while res and res[-1] != '[':
                    temp = res[-1] + temp
                    res = res[:-1]
    
                res = res[:-1]
    
                num = ""
                while res and res[-1].isdigit():
                    num = res[-1] + num
                    res = res[:-1]
                p = int(num)
    
                res += temp * p
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends
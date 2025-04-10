class Solution:
    def maxPartitions(self , s):
        last_index=[-1]*26
        
        for i in range(len(s)-1,-1,-1):
            if last_index[ord(s[i])-ord('a')]==-1:
                last_index[ord(s[i])-ord('a')]=i
                
        count=0
        end=-1
        
        for i in range(len(s)):
            end=max(last_index[ord(s[i])-ord('a')],end)
            
            if i==end:
                count+=1
                
        return count

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends
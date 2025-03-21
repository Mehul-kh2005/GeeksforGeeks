class Solution:
    def subarrayXor(self, arr, k):
        xor=0
        count=0
        xor_freq={0:1}
        
        for num in arr:
            xor^=num
            if xor^k in xor_freq:
                count+=xor_freq[xor^k]
                
            xor_freq[xor]=xor_freq.get(xor,0)+1
            
        return count

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
import heapq

class Solution:
	def kLargest(self, arr, k):
		arr=[-num for num in arr]
		heapq.heapify(arr)
		result=[]
		while k!=0:
		    result.append(-(heapq.heappop(arr)))
		    k-=1
		    
		return result
		
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
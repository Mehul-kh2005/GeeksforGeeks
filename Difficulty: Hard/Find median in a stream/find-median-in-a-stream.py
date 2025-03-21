import heapq

class Solution:
    def getMedian(self, arr):
        left_max_heap=[]
        right_min_heap=[]
        result=[]
        
        for num in arr:
            heapq.heappush(left_max_heap,-num)
            
            heapq.heappush(right_min_heap,-heapq.heappop(left_max_heap))
            
            if len(right_min_heap)>len(left_max_heap):
                 heapq.heappush(left_max_heap,-heapq.heappop(right_min_heap))
                 
            if len(left_max_heap)!=len(right_min_heap):
                result.append(-left_max_heap[0])
                
            else:
                result.append((-left_max_heap[0]+right_min_heap[0])/2)
                
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends
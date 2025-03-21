#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import heapq

class Solution:
    def squared_distance(self,point):
        return point[0]**2 + point[1]**2
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]
        for point in points:
            distance=self.squared_distance(point)
            
            if len(max_heap)<k:
                heapq.heappush(max_heap,(-distance,(point)))
            
            else:
                if -distance>max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap,(-distance,(point)))
                    
        return [pair[1] for pair in max_heap]


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends
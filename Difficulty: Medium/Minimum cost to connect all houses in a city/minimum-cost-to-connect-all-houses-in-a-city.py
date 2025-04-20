import heapq

class Solution:
    def manhattanDistance(self,u,v):
        return abs(u[0]-v[0])+abs(u[1]-v[1])
        
    def minCost(self, houses):
        n=len(houses)
        min_heap=[(0,0)]
        visited=[False]*n
        total_cost=0
        connected=0
          
        while min_heap:
            cost,u=heapq.heappop(min_heap)
            
            if visited[u]:
                continue
              
            visited[u]=True
            total_cost+=cost
            connected+=1
            
            if connected==n:
                break
              
            for v in range(n):
                if not visited[v]:
                    dist=self.manhattanDistance(houses[u],houses[v])
                    heapq.heappush(min_heap,(dist,v))
        
        return total_cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends
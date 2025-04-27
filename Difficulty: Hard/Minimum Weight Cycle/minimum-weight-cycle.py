import heapq

class Solution:
    def constructAdj(self,V:int,edges:list[int])->list[int]:
        adjList=[[] for _ in range(V)]
        
        for u,v,w in edges:
            adjList[u].append([v,w])
            adjList[v].append([u,w])
        
        return adjList
        
        
    def shortestPath(self,V,adjList,src,dest):
        distance=[float('inf')]*V
        distance[src]=0
        
        queue=[(0,src)]
        
        while queue:
            currDist,u=heapq.heappop(queue)
            
            if currDist>distance[u]:
                continue
            
            for v,w in adjList[u]:
                if (u==src and v==dest) or (u==dest and v==src):
                    continue
                
                if distance[v]>currDist+w:
                    distance[v]=currDist+w
                    heapq.heappush(queue,(distance[v],v))
                
        return distance[dest]
        
        
    def findMinCycle(self, V, edges):
        minWeight=float('inf')
        adjList=self.constructAdj(V,edges)
        
        for u,v,w in edges:
            dist=self.shortestPath(V,adjList,u,v)
            
            if dist!=float('inf'):
                minWeight=min(minWeight,dist+w)
                
        return minWeight

#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        obj = Solution()
        res = obj.findMinCycle(V, edges)

        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends
import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adjList=[[] for _ in range(V)]
        
        for u,v,w in edges:
            adjList[u].append((v,w))
            adjList[v].append((u,w))
            
        distances=[float('inf')]*V
        distances[src]=0
        min_heap=[(0,src)]
        
        while min_heap:
            curr_dist,u=heapq.heappop(min_heap)
            
            for v,weight in adjList[u]:
                if curr_dist+weight<distances[v]:
                    distances[v]=curr_dist+weight
                    heapq.heappush(min_heap,(distances[v],v))
                
        return distances

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

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
from collections import deque

class Solution:
    def constructAdj(self,V,edges,c,d):
        adjList=[[] for _ in range(V)]
        
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c):
                continue
            
            adjList[u].append(v)
            adjList[v].append(u)
        
        return adjList
        
    def isBridge(self, V, edges, c, d):
        adjList=self.constructAdj(V,edges,c,d)
        visited=[False]*V
        
        queue=deque([c])
        
        while queue:
            node=queue.popleft()
            visited[node]=True
            
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                
        return not visited[d]

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
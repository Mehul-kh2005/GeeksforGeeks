class Solution:
    def constructAdj(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj
    
    def findPoints(self, adj, u, visited, disc, low, time, parent, isAP):
        
        visited[u] = 1
        time[0] += 1
        disc[u] = low[u] = time[0]
        children = 0
    
        for v in adj[u]:
            
            if not visited[v]:
                children += 1
                self.findPoints(adj, v, visited, disc, low, time, u, isAP)
    
                low[u] = min(low[u], low[v])
    
                if parent != -1 and low[v] >= disc[u]:
                    isAP[u] = 1
    
            elif v != parent:
                low[u] = min(low[u], disc[v])
                
        if parent == -1 and children > 1:
            isAP[u] = 1
    
    def articulationPoints(self, V, edges):
        adj = self.constructAdj(V, edges)
        disc = [0] * V
        low = [0] * V
        visited = [0] * V
        isAP = [0] * V
        time = [0]  
        
        for u in range(V):
            if not visited[u]:
                self.findPoints(adj, u, visited, disc, low, time, -1, isAP)
    
        result = [u for u in range(V) if isAP[u]]
    
        return result if result else [-1]
    
#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends
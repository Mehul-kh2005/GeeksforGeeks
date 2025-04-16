from collections import deque

class Solution:
    def constructAdj(self,V,edges):
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            
        return adjList
        
    def topoSort(self, V, edges):
        adjList=self.constructAdj(V,edges)
        indegree=[0]*V
        
        for u in range(V):
            for v in adjList[u]:
                indegree[v]+=1
                
        queue=deque([i for i in range(V) if indegree[i]==0])
        result=[]
        
        while queue:
            node=queue.popleft()
            result.append(node)
            
            for neighbor in adjList[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
                    
        return result

#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        x = V
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, x, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
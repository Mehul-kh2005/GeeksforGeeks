from collections import deque

class Solution:
    def constructAdj(self,V,edges):
        adjList=[[] for _ in range(V)]
        
        for u,v in edges:
            adjList[u].append(v)
            
        return adjList
        
    def isCycle(self, V, edges):
        adjList=self.constructAdj(V,edges)
        indegree=[0]*V
        
        for i in range(V):
            for j in adjList[i]:
                indegree[j]+=1
                
        queue=deque([i for i in range(V) if indegree[i]==0])
        count=0
        
        while queue:
            node=queue.popleft()
            count+=1
            
            for neighbor in adjList[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
                    
        return count!=V

#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends
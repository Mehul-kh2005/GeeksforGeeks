from collections import deque

class Solution:
    def bfs(self,start,adjList,visited):
        queue=deque([(start,-1)])
        visited[start]=True
        
        while queue:
            node,parent=queue.popleft()
            
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append((neighbor,node))
                    
                elif neighbor!=parent:
                    return True
                    
        return False
        
    def constructAdj(self,V,edges):
        adjList=[[] for _ in range(V)]
        
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        return adjList
        
	def isCycle(self, V, edges):
		adjList=self.constructAdj(V,edges)
		visited=[False]*V
		
		for i in range(V):
		    if not visited[i]:
		        if self.bfs(i,adjList,visited):
		            return True
		            
		return False

#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


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
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
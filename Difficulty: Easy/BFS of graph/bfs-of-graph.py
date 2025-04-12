#User function Template for python3
from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n=len(adj)
        visited=[False]*n
        result=[]
        queue=deque()
        
        visited[0]=True
        queue.append(0)
        
        while queue:
            node=queue.popleft()
            result.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append(neighbor)
                    
        return result
        
#{ 
 # Driver Code Starts
import sys
from queue import Queue
from typing import List


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
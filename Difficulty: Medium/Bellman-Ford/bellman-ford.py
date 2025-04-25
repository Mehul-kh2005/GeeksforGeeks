#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        distance=[10**8]*V
        distance[src]=0
        
        for i in range(V):
            for u,v,w in edges:
                if distance[u]!=10**8 and distance[u]+w<distance[v]:
                    if i==V-1:
                        return [-1]
                    
                    distance[v]=distance[u]+w
                    
        return distance

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
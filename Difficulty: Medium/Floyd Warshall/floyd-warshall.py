#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		V=len(dist) # No. of Vertices
		
		for k in range(V):
		    for i in range(V):
		        for j in range(V):
		            if (dist[i][k]!=10**8) and (dist[k][j]!=10**8):
		                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
		                
		return dist
		
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.floydWarshall(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends
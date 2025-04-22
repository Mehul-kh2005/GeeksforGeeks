from collections import deque

#BFS Approach
class Solution:
    def isSafe(self,image,n,m,row,col,originalColor):
        return (0<=row<n and 0<=col<m) and (image[row][col]==originalColor)
    
	def floodFill(self, image, sr, sc, newColor):
	    n=len(image)
	    m=len(image[0])
		
		queue=deque([(sr,sc)])
		directions=[(1,0),(-1,0),(0,1),(0,-1)]
		originalColor=image[sr][sc]
		
		if originalColor==newColor:
		    return image
		
		while queue:
		    row,col=queue.popleft()
		    image[row][col]=newColor
		    
		    for r,c in directions:
		        newRow=row+r
		        newCol=col+c
		        
		        if self.isSafe(image,n,m,newRow,newCol,originalColor):
		            queue.append((newRow,newCol))
		
		return image
		

'''
#DFS Approach
class Solution:
    def dfs(self,image,n,m,row,col,originalColor,newColor):
        if (row<0 or row>=n) or (col<0 or col>=m) or (image[row][col]!=originalColor):
            return
        
        image[row][col]=newColor
            
        self.dfs(image,n,m,row+1,col,originalColor,newColor)
        self.dfs(image,n,m,row-1,col,originalColor,newColor)
        self.dfs(image,n,m,row,col+1,originalColor,newColor)
        self.dfs(image,n,m,row,col-1,originalColor,newColor)
    
    def floodFill(self, image, sr, sc, newColor):
        n=len(image)
        m=len(image[0])
        originalColor=image[sr][sc]
		
		if originalColor==newColor:
		    return image
		    
		self.dfs(image,n,m,sr,sc,originalColor,newColor)
		
		return image
'''

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends
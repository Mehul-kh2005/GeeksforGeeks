#User function Template for python3

class Solution:
    def isSafe(self,grid,row,col):
        return (0<=row<len(grid)) and (0<=col<len(grid[0])) and (grid[row][col]=='L')
        
    def dfs(self,grid,r,c):
        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for nr,nc in directions:
            newRow=r+nr
            newCol=c+nc
            
            if self.isSafe(grid,newRow,newCol):
                grid[newRow][newCol]='W'
                self.dfs(grid,newRow,newCol)
                
            
    def numIslands(self, grid):
        count=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='L':
                    self.dfs(grid,row,col)
                    count+=1
                    
        return count

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends
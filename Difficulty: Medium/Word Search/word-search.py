class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[index]:
                return False
            
            temp = mat[i][j]
            mat[i][j] = '#' 
            
            for di, dj in directions:
                if dfs(i + di, j + dj, index + 1):
                    return True
            
            mat[i][j] = temp  
            return False
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
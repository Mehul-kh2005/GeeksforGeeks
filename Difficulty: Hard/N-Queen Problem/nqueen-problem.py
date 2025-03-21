#User function Template for python3

class Solution:
    def nQueen(self, n):
        def is_safe(row, col, diagonals, anti_diagonals, rows):
            return (row not in rows and
                    (row - col) not in diagonals and
                    (row + col) not in anti_diagonals)

        def backtrack(col, diagonals, anti_diagonals, rows, state):
            if col == n:
                result.append([row + 1 for row in state])  
                return

            for row in range(n):
                if is_safe(row, col, diagonals, anti_diagonals, rows):
                    rows.add(row)
                    diagonals.add(row - col)
                    anti_diagonals.add(row + col)
                    state.append(row)

                    backtrack(col + 1, diagonals, anti_diagonals, rows, state)

                    rows.remove(row)
                    diagonals.remove(row - col)
                    anti_diagonals.remove(row + col)
                    state.pop()

        result = []
        backtrack(0, set(), set(), set(), [])
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends
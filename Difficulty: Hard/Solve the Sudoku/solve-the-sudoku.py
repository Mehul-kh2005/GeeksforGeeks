#User function Template for python3

class Solution:
    def solveSudoku(self, mat):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        self.empty_cells = []
        for i in range(9):
            for j in range(9):
                num = mat[i][j]
                if num != 0:
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[(i // 3) * 3 + (j // 3)].add(num)
                else:
                    self.empty_cells.append((i, j))

        self.solve(mat, 0)

    def solve(self, mat, idx):
        if idx == len(self.empty_cells):
            return True

        row, col = self.empty_cells[idx]
        box_idx = (row // 3) * 3 + (col // 3)

        for num in range(1, 10):
            if num not in self.rows[row] and num not in self.cols[col] and num not in self.boxes[box_idx]:
                mat[row][col] = num
                self.rows[row].add(num)
                self.cols[col].add(num)
                self.boxes[box_idx].add(num)

                if self.solve(mat, idx + 1):
                    return True

                mat[row][col] = 0
                self.rows[row].remove(num)
                self.cols[col].remove(num)
                self.boxes[box_idx].remove(num)

        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends
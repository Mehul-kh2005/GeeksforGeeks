#User function Template for python3

class Solution:
    # Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # Sort the array
        arr.sort()
        n = len(arr)
        count = 0

        # Iterate from the last element to the third element
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1

            # Use two pointers to find pairs that satisfy the triangle inequality
            while i < j:
                # Check if arr[i] + arr[j] > arr[k]
                if arr[i] + arr[j] > arr[k]:
                    # All pairs between i and j will satisfy the inequality
                    count += (j - i)
                    j -= 1
                else:
                    # Increment i to try a larger value
                    i += 1

        return count
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends
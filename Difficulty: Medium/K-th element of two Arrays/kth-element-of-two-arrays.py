#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        if len(a) > len(b):
            return self.kthElement(b, a, k)
        
        n, m = len(a), len(b)
        low, high = max(0, k - m), min(k, n)
        
        while low <= high:
            cut_a = (low + high) // 2
            cut_b = k - cut_a
            
            left_a = a[cut_a - 1] if cut_a > 0 else float('-inf')
            left_b = b[cut_b - 1] if cut_b > 0 else float('-inf')
            right_a = a[cut_a] if cut_a < n else float('inf')
            right_b = b[cut_b] if cut_b < m else float('inf')
            
            if left_a <= right_b and left_b <= right_a:
                return max(left_a, left_b)
            elif left_a > right_b:
                high = cut_a - 1
            else:
                low = cut_a + 1
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
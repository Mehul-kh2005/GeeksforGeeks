#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # Sort the array to use the two-pointer approach
        arr.sort()
        n = len(arr)
        closest_pair = []
        closest_diff = float('inf')  # Initialize with a large value

        # Two-pointer technique
        left, right = 0, n - 1

        while left < right:  # Fix: Change <= to <
            # Calculate the sum of the two pointers
            current_sum = arr[left] + arr[right]
            current_diff = abs(target - current_sum)

            if current_diff < closest_diff:
                # Update the closest difference and closest pair
                closest_diff = current_diff
                closest_pair = [arr[left], arr[right]]
            elif current_diff == closest_diff:
                # Check for maximum absolute difference
                if abs(arr[right] - arr[left]) > abs(closest_pair[1] - closest_pair[0]):
                    closest_pair = [arr[left], arr[right]]

            # Move pointers based on the current sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If the sum equals the target, return immediately
                return closest_pair

        return closest_pair if closest_pair else []





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
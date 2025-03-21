class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0

        # Iterate through each element as the first element of the triplet
        for i in range(n - 2):
            left = i + 1
            right = n - 1

            # Use two-pointer approach to find triplets
            while left < right:
                # Calculate the sum of the triplet
                triplet_sum = arr[i] + arr[left] + arr[right]

                # If sum is equal to target, count it
                if triplet_sum == target:
                    # Move both pointers inward, and directly count all valid pairs
                    if arr[left] == arr[right]:
                        count += (right - left + 1) * (right - left) // 2
                        break

                    left_count = 1
                    right_count = 1

                    # Count frequency of current value at 'left'
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        left_count += 1

                    # Count frequency of current value at 'right'
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        right_count += 1

                    # Add all combinations of valid pairs
                    count += left_count * right_count

                    # Move both pointers inward
                    left += 1
                    right -= 1

                # If sum is smaller, move to bigger values
                elif triplet_sum < target:
                    left += 1

                # If sum is greater, move to smaller values
                else:
                    right -= 1

        return count







#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends
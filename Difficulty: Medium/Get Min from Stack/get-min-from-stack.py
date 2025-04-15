class Solution:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    # Add an element to the top of Stack
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x<=self.min_stack[-1]:
            self.min_stack.append(x)
        
    # Remove the top element from the Stack
    def pop(self):
        if self.stack:
            if self.stack[-1]==self.min_stack[-1]:
                self.min_stack.pop()
                
            self.stack.pop()

    # Returns top element of Stack
    def peek(self):
        return self.stack[-1] if self.stack else -1

    # Finds minimum element of Stack
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1

#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends
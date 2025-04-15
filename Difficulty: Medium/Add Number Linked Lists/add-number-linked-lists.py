#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Reverse both lists to simplify addition
        num1 = reverse_list(num1)
        num2 = reverse_list(num2)

        carry = 0
        result_head = None
        result_tail = None

        # Add numbers until both lists are exhausted
        while num1 or num2 or carry:
            val1 = num1.data if num1 else 0
            val2 = num2.data if num2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            # Create a new node for the digit
            new_node = Node(digit)
            if result_head is None:
                result_head = result_tail = new_node
            else:
                result_tail.next = new_node
                result_tail = new_node

            # Move to the next nodes
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next

        # Reverse the result to restore the correct order
        result_head = reverse_list(result_head)

        # Remove leading zeros if present
        while result_head and result_head.data == 0:
            result_head = result_head.next

        # If all nodes are removed (result is 0), create a single node with value 0
        if not result_head:
            return Node(0)

        return result_head

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends
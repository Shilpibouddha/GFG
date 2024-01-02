# User function Template for Python3

# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, N, head):
        
       
        if head is None:
            return None  # Handle empty linked list
        
        es, ee, os, oe = None, None, None, None
        current = head

        while current is not None:
            x = current.data

            if x % 2 == 0:
                if es is None:
                    es = current
                    ee = es
                else:
                    ee.next = current
                    ee = ee.next
            else:
                if os is None:
                    os = current
                    oe = os
                else:
                    oe.next = current
                    oe = oe.next

            current = current.next

        if os is None or es is None:
            return head  # No need to rearrange

        ee.next = os
        oe.next = None

        return es


#{ 
 # Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(n, list1.head)
        printlist(newhead)


# } Driver Code Ends
#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
        # reverse the first linked list
# reverse the second linked list
# start adding the data with a while loop, if sum>9 take a carry to the next data else add simply
# check at last if carry exists, add the carry to the linked list
# reverse the final linked list and return result
    def addTwoLists(self, first, second):
        

        def reverse(head):
            cur=head
            prev=None
            
            while(cur):
                nex=cur.next
                cur.next=prev
                prev=cur
                cur=nex
            
            return prev
        
        ll1=reverse(first)
        ll2=reverse(second)
        resll=Node(0)
        a=resll
        carry=0
        while(ll1 and ll2):
            num=ll1.data + ll2.data + carry
            if num>9:
                q=num//10
                r=num%10
                numNode=Node(r)
                resll.next=numNode
                carry=q
            else:
                numNode=Node(num)
                resll.next=numNode
                carry=0
            resll=resll.next
            ll1=ll1.next
            ll2=ll2.next
        
        while(ll1):
            num=ll1.data+carry
            if num>9:
                q=num//10
                r=num%10
                numNode=Node(r)
                resll.next=numNode
                carry=q
            else:
                numNode=Node(num)
                resll.next=numNode
                carry=0
            resll=resll.next
            ll1=ll1.next
        
        while(ll2):
            num=ll2.data+carry
            if num>9:
                q=num//10
                r=num%10
                numNode=Node(r)
                resll.next=numNode
                carry=q
            else:
                numNode=Node(num)
                resll.next=numNode
                carry=0
            resll=resll.next
            
            ll2=ll2.next
        
        if carry>0:
            numNode=Node(carry)
            resll.next=numNode
        
        final=reverse(a.next)
        
        return final
        

    

       
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
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
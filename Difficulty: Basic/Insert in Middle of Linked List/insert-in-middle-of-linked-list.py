#User function Template for python3
'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
def insertInMid(head,node):
    if head is None:
        # If the list is empty, insert the new node as the only element.
        return node
    
    # Use two pointers technique to find the middle
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    node.next = slow.next
    slow.next = node
    
    return head
    
                
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the 
    #linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return
    
    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print('')

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        mid_elem = int(input())
        insertInMid(a.head, Node(mid_elem) )
        a.printList()
# } Driver Code Ends
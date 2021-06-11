class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        if head is None:
            return None
        
        #taking three pointers to store the current, previous and next nodes.
        prev = None
        current = head
        next = current.next
        
        
        while current is not None:
            #taking the next node as next.
            next = current.next 
            
            #storing the previous node in link part of current node.
            current.next = prev 
            
            #updating prev from previous node to current node.
            prev = current
            
            #updating current node to next node.
            current = next           
        
        return prev
      
class Node:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def insert(self, val):
    if self.head is None:
      self.head = Node(val)
      self.tail = self.head
    else:
      self.tail.next = Node(val)
      self.tail = self.tail.next
      
def printList(head):
  tmp = head
  while tmp:
    print(tmp.data, end = '')
    tmp = tmp.next
  print()

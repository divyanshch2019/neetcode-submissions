import sys
class Node:
    def __init__(self,val=0,min_val=sys.maxsize,prev=None,next=None):
        self.val,self.min_val = val,min_val
        self.prev,self.next = prev, next
class MinStack:

    def __init__(self):
        self.head = Node()
        self.first = self.head
        

    def push(self, val: int) -> None:
        newNode = Node(val,min(val,self.first.min_val))
        self.first.next =  newNode
        newNode.prev = self.first
        self.first = newNode
        

    def pop(self) -> None:
        if self.first!=self.head:
            oldTop = self.first
            self.first = oldTop.prev
        

    def top(self) -> int:
        return self.first.val
        

    def getMin(self) -> int:
        return self.first.min_val
        

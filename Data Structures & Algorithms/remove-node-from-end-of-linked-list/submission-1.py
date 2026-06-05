# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the linked list
        # if the difference of the length and the n is <=1 return head.next
        # other wise loop through the list and delete the nth element

        def list_len(node):
            result = 0
            while node:
                result+=1
                node = node.next
            return result
        
        current = head
        length = list_len(current)
        node_to_delete = length - n
        prev = None
        while current:
            if node_to_delete == 0:
                #delete the current node
                if not prev:
                    #this is the first iteration of the loop
                    return head.next
                prev.next = current.next
                return head
            node_to_delete-=1
            prev = current
            current = current.next
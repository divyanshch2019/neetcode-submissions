# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the mid
        #reverse from the mid
        #reassemble the list
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow would be the mid
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev=  second
            second = temp
        first,second = head,prev
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head

        self.swapPairs(head.next.next)

        temp = head.val
        head.val = head.next.val
        head.next.val = temp

        return head
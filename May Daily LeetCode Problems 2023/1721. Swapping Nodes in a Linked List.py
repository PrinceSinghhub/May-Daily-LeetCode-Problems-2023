# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head, k):

        # Find kth node from left
        l = r = head
        for _ in range(k - 1):
            l = l.next
        # Find kth node from right
        # by finding tail node
        tail = l
        while tail.next != None:
            r, tail = r.next, tail.next
        # Swap values and return
        l.val, r.val = r.val, l.val
        return head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        itr = None
        # while the head is none,
        # move itr to the head, shift head over next, move itr.next to point to object before
        # increment from object before
        while head:
            itr = head
            head = itr.next
            itr.next = prev
            prev = itr
        return itr

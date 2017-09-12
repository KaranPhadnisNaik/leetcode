# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # O(n)
        # if no LL or one Node in LL or k =0, return head
        if not head or not head.next or k==0:
            return head
        # count the length of the list
        count = 0
        itr = head
        while itr.next:
            count += 1
            itr = itr.next
        count += 1

        # if we need to make any multiple of 'count' rotations we return the original list
        k = k % count
        if k == 0:
            return head

        # we connect the ends together
        itr.next = head
        movements = count - k
        # we want to stop at the last element of this new list
        for i in range(movements):
            itr = itr.next
        # now itr is on the last element of the new list
        head = itr.next
        itr.next = None
        return head

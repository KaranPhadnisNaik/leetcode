# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # if empty or one element with next == None
        if not head or not head.next:
            return False
         # we know head and head next exist so assign a fast itr to head next and slow itr to head
        slow = head
        fast = head.next
        # while they are not equal
        while fast is not slow:
            # since we know fast does exist, we need to check if the next 2 nodes exists too so that fast can iterate
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

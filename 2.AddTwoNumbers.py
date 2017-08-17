# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, list1, list2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if empty
        if not list1 and not list2:
            return ListNode(0)
        #itrs and carry vars
        head = itr = ListNode(0)
        carry = 0
        # while all the values are not none or carry isnt 0
        while list1 or list2 or carry:
            total = (list1.val if list1 else 0) + (list2.val if list2 else 0) + carry
            digit, carry = total%10, total//10
            #append the digit to the finalList
            itr.next = ListNode(digit)
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
            itr = itr.next
        return head.next

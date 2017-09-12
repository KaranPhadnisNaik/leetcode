class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # no palindrome if negative
        # no palindrome if more than 32 bit int
        if x >= 2**31-1 or x<0:
            return False
        # number wont have leading zeros so cant end in zero, unless the entire number is zero
        if x%10 ==0 and x != 0:
            return False

        new=0
        while new <= x:
            if new == x: # works for even lenth of number
                return True
            new = new*10 + x%10
            x /= 10
        # if the newly formed number is larger than 32 bit int you fail
        if new >= 2**31-1:
            return False
        # since newly formed number is greater than x,
            # floor division by 10 would give it same # of digits as x
        return (new/10 == x)

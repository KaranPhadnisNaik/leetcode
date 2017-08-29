class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # zero , positive, negative
        if num  == 0:
            return str(num)
        final = ""
        sign = '-' if num < 0 else ''
        num = abs(num)
        while num:
            final = str(num%7) + final
            num /= 7
        return sign+final


        

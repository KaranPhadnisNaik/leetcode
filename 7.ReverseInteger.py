class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > (2**31-1) or x < -(2**31-1):
            return 0
        abs_int = abs(x)
        final = 0
        # while x is not zero
        while abs_int:
            final = final*10 + abs_int%10
            abs_int /= 10
        if final > (2**31-1) or final < -(2**31-1):
            return 0
        return final if x >= 0 else final*(-1)

        

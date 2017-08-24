class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        # naive
        i =0
        while(i*i < x):
            i += 1
        return i
        """
        # binary search
        if x < 0:
            return False
        if x == 0 or x == 1:
             return x
        left = 1
        right = x
        mid = (left+right)/2
        while True:
            # check if middle value is sqrt of x
            if mid*mid == x:
                break
            # if right and left right no more than 1 away, the sqrt of x is between right and left
            # so return the middle value (floored)
            if abs(right-left) == 1:
                break
            elif mid*mid > x:
                right = mid
                mid = (left+right)/2
            elif mid*mid < x:
                left = mid
                mid = (left+right)/2
        return mid

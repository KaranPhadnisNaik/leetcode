class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        l = 1
        r = num
        mid = (r+l)/2
        # we know the sqrt of num will be less than num
        # perform binary search to check if a number exists (mid) s.t. mid**2 = num
        while True:
            if mid*mid == num:
                break
            if abs(r-l) == 1:
                return False
            if mid*mid > num:
                r = mid
                mid = (r+l)/2
            elif mid*mid < num:
                l = mid
                mid = (r+l)/2
        return True

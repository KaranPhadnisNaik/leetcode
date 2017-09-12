class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if zero as exponent or 1 as base, return 1
        if n == 0 or x == 1:
            return 1
        # for negative exponents, reciprocate
        if n < 0:
            x = 1/x
            n *= -1
        # O(log(n))
        if n%2==1:
            return x*self.myPow(x*x,n//2)
        return self.myPow(x*x,n//2)

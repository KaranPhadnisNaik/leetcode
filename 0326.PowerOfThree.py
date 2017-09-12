class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # check if n is positive and n divides into the largest possible 32 bit int
        # power of 3
        return ( n>0 and (3**19)%n==0)
        

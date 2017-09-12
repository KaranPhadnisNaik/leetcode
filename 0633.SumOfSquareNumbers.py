class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        #  its not necessary to iterate through all c numbers
        #  if a**2 + b**2 = c
        # then a**2 = c - b**2
        # then a = sqrt(c - b**2)
        # b => [0, sqrt(c)]
        # c will never be non negative so we dont need to look at negative values for
        #   a and b

        # Linear search:
        # O(sqrt(c)) Time (assuming square root is O(1))

        for b in range(int(c**(.5))+1):
            # check if the float form is equal to the integer (ex, does 3.0 == 3)
            a = (c-b**2)**(.5)
            if int(a) == a:
                return True
        return False

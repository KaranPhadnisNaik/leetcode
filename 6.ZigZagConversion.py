class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 0:
            return None
        if numRows == 1:
            return s

        # each index represents a stage in the cycle
        vals = [''] * numRows
        # value that iterates through the cycle
        index = 0
        direction = 0
        for ch in s:
            vals[index] += ch
            # we need to step up
            if index == 0:
                direction = 1
            elif index == numRows-1:
                direction = -1
            index += direction
        return ''.join(vals)
                

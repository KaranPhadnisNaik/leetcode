import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # we know that the max possible area is via square
        root = int(math.sqrt(area))

        # keep reducing length by 1 until we get area
        while area % root != 0:
            root -= 1
        return [area/root ,root]

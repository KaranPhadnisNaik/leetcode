class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # since we should assign the biggest cookie to the greediest kid,
        # it would be best to sort g and s
        g = sorted(g)
        s = sorted(s)
        count = 0
        i = 0 #cookie
        j = 0 #kids
        while i < len(s) and j < len(g):
            if s[i] >= g[j]: # if that cookie statisfies the kid's greed
                count += 1
                j += 1
            i += 1
        return count
        

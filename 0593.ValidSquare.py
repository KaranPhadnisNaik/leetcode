class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance(p1,p2):
            return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 )

        # if we count the distance from each from each other we will have 6 distances
        # out of those six distances 4 should represent the sides of the squares and
        # the other 2 should represent the diagonals

        # store the values in a dictionary st that key is the length b/w the points and key is
        # the count
        solns = {}
        p = [p1,p2,p3,p4]
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                d = str(distance(p[i],p[j]))
                if not d in solns:
                    solns[d] = 1
                else:
                    solns[d] += 1
        return len(solns)==2 and 2 in solns.values() and 4 in solns.values()

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return None
        # top 3 values
        largeMax = float('-inf')
        midMax = float('-inf')
        smallMax = float('-inf')

        # get the bottom 2 values (since multiplying them both will give us a positive num)
        smallMin = float('inf')
        largeMin = float('inf')

        for num in nums:
            if num > largeMax:
                largeMax, midMax, smallMax = num, largeMax, midMax
            elif num > midMax:
                midMax, smallMax = num, midMax
            elif num > smallMax:
                smallMax = num

            if num < smallMin:
                smallMin, largeMin = num, smallMin
            elif num < largeMin:
                largeMin = num

        return max(largeMax*midMax*smallMax, largeMax*smallMin*largeMin)
        

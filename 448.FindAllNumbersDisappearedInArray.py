class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # somehow we need to know whether there are/is value(s) between [1,n] that don't exist
        # 1) when a value is found, we convert the value at the index corresponding to the original value
        #    (if the array was sorted) to negative
        #        ex. since 4 is in [4,2,1,2] => [4,2,1,-2]
        # 2) then return the indexes of the values in the array that are still positive
        # and that will give us the missing values

        #O(2n) ===> O(n)
        i =0
        while (i < len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] *= -1
            i += 1
        final = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                final.append(i+1)
        return final




        

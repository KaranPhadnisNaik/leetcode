class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solns = {}
        for i in range(len(nums)):
            if nums[i] not in solns:
                solns[target-nums[i]] = i
            else:
                return [solns[nums[i]],i]
        

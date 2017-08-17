class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        elif len(nums)==3:
            return [nums] if sum(nums)==0 else []

        #sort (assuming nlogn)
        nums = sorted(nums)

        soln = []

        for i in range(len(nums)-2):
            # we also want to avoid duplicates when it comes to i
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip the rest of the iteration
            beg = i+1
            end = len(nums)-1
            while(beg < end):
                tot = nums[i] + nums[beg] + nums[end]
                if tot==0:
                    soln.append([nums[i], nums[beg], nums[end]])
                    # we need to adjust for duplicates so move beg and end so that you avoid
                    # any duplicate values
                    while beg < end and nums[beg] == nums[beg+1]:
                        beg += 1
                    while beg < end and nums[end] == nums[end-1]:
                        end -= 1
                    # now we've reached the last possible instance of that repeated value so
                    # increment both 1 in their respective directions
                    beg += 1
                    end -= 1
                elif tot < 0:
                    beg += 1
                else:
                    end -= 1
        return soln




        

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set([])
        
        for i in range(len(nums)):
            
            l = i + 1
            r = len(nums) - 1
            
            while(l < r):
                sum_ = nums[i] + nums[l] + nums[r]

                if sum_ == 0:
                    result.add((nums[i] , nums[l] , nums[r]))
                    l += 1
                    r -= 1

                elif(sum_ > 0):
                    r -= 1

                else:
                    l += 1

        return list(result)

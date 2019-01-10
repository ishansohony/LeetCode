class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right, count = {}, {}, {}
        
        for i in range(len(nums)):
            
            if nums[i] not in count:
                count[nums[i]] = 1
                left[nums[i]] = i
                right[nums[i]] = i
            else:
                count[nums[i]] += 1
                right[nums[i]] = i
                
            
        degree = max(count.values())
        
        ma = len(nums)
        
        for i in count:
            if count[i] == degree:
                ma = min(ma, right[i] - left[i] + 1)
                
        return ma

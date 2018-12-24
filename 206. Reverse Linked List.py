class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastnonzero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[lastnonzero], nums[curr] = nums[curr], nums[lastnonzero]
                lastnonzero += 1
                
        

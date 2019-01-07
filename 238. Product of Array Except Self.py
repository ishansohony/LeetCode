class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        left = [0]*n
        left[0] = 1
        
        for i in range(1, n):
            left[i] = nums[i-1]*left[i-1]
        
        right = [0]*n
        right[-1] = 1
        cnt = n - 2
        
        while(cnt >= 0):    
            right[cnt] = nums[cnt+1] * right[cnt+1]
            cnt -= 1
        
        result = []
        
        for i in range(n):
            result.append(left[i]*right[i])
            
        return result

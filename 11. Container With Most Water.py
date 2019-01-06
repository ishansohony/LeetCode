class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l, r = 0, len(height) - 1
        ma = 0
        
        while(l < r):
            ca = min(height[l], height[r]) * (r - l)
            ma = max(ma, ca)
            
            if(height[l] < height[r]):
                l += 1
                
            else:
                r -= 1
                
        
        return ma
        

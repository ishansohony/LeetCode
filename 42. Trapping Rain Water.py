class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        n = len(height)
        lm = [0]*n
        rm = [0]*n
        lm[0] = height[0]
        rm[-1] = height[-1]
        tw = 0
        
        for i in range(1,n):
            lm[i] = max(height[i], lm[i - 1])
        
        for i in range(n - 2, -1, -1):
            rm[i] = max(height[i], rm[i + 1])
        
        for i in range(n):
            tw += min(rm[i], lm[i]) - height[i]
        
        return tw

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        
            
        
        def getp(i,j,s):
            while((i >= 0) and (j < len(s)) and (s[i] == s[j])):
                i -= 1
                j += 1
                
            return s[i+1:j]
        
        max_l = -1
        for i in range(len(s)):
            l1 = getp(i,i,s)
            l2 = getp(i,i+1,s)
            
            if len(l1) > max_l:
                res = l1
                max_l = len(l1)
            
            if len(l2) > max_l:
                res = l2
                max_l = len(l2)
                
        return res

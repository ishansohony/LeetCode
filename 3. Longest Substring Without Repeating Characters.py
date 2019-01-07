class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = j = 0
        seen = set()
        max_len = 0
        
        while(j < len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1
                
                
        return max_len

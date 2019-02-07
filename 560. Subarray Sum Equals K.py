class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sdict = collections.Counter()
        sdict[0] = 1
        kcnt = 0
        cs = 0
        for i in nums:
            cs += i
            if cs - k in sdict:
                kcnt += sdict[cs - k]
            sdict[cs] += 1
        
        return kcnt
        

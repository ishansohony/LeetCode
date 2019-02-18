class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        
        set1 = set(nums)
        set2 = set()
        max_len = 0
        for num in set1:
            l = 0
            if num not in set2:
                temp = num
                while temp in set1:
                    set2.add(temp)
                    l += 1
                    temp = temp - 1
                
                temp = num + 1
                while temp in set1:
                    set2.add(temp)
                    l += 1
                    temp = temp + 1
                max_len = max(max_len, l)
        
        return max_len
                
                
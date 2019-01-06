# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        intervals.sort(key = lambda tup: tup.start)
        
        return_list = []
        
        for i in intervals:
            
            if not return_list:
                return_list.append(i) 
            
            if i.start <= return_list[-1].end:
                return_list[-1].end = max(i.end, return_list[-1].end)
            
            else:
                return_list.append(i)
                
            
        return return_list

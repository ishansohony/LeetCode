# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        st = []
        et = []
        
        for i in intervals:
            st.append(i.start)
            et.append(i.end)
            
        st.sort()
        et.sort()
        
        sp, ep = 0,0
        rooms = 0
        
        while sp < len(st):
            
            if st[sp] >= et[ep]:
                rooms -= 1
                ep += 1
                
            
            rooms += 1
            sp += 1
            
        return rooms

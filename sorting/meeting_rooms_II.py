'''
253. Meeting Rooms II
Medium

2109

31

Add to List

Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

from typing import List
from queue import PriorityQueue

class Solution:


    def minMeetingRooms(self, intervals: List[List[int]]):
        
        if intervals == None or len(intervals) == 0:
            return 0

        if len(intervals) == 1:
            return 1

        intervals.sort(key=lambda x: x[0])

        room_q = PriorityQueue()
        room_q.put(intervals[0][1])

        for i in range(1, len(intervals)):

            if not room_q.empty() and intervals[i][0] >= room_q.queue[0]:
                room_q.get()
                room_q.put(intervals[i][1])
            else:
                room_q.put(intervals[i][1])
        
        return len(room_q.queue)


        


# nums = [[0, 30],[5, 10],[15, 20]]
# nums = [[7,10],[2,4]]
nums = None
sol = Solution()
print(sol.minMeetingRooms(nums))

        
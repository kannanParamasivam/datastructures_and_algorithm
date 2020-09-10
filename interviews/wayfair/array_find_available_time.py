'''
We are writing a tool to help users manage their calendars. Given an unordered list of times of day when people are busy, write a function that tells us the intervals during the day when ALL of them are available.

Each time is expressed as an integer using 24-hour notation, such as 1200 (12:00), 1530 (15:30), or 800 (8:00).

Sample input:
'''

p1_meetings = [
  (1230, 1300),
  ( 845, 900),
  (1300, 1500),
]

p2_meetings = [
  ( 0, 844),
  ( 930, 1200),
  (1515, 1546),
  (1600, 2400),
]

p3_meetings = [
  ( 845, 915),
  (1515, 1545),
  (1235, 1245),
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]

'''
Expected output:

findAvailableTime(schedules1)
 => [   844,  845 ],
    [  915,  930 ],
    [ 1200, 1230 ],
    [ 1500, 1515 ],
    [ 1546, 1600 ]

findAvailableTime(schedules2)
 => [    0,  845 ],
    [  915, 1230 ],
    [ 1500, 1515 ],
    [ 1545, 2400 ]
'''

from queue import PriorityQueue


def findAvailableTime(schedules):
    
    if not schedules:
        return
    
    min_heap = PriorityQueue()
    
    for schedule in schedules:
        
        for meeting in schedule:
            
            min_heap.put(meeting)
            
    min_heap.put((2400, 2400))
    
    prev_end = 0
    res = []
    
    while not min_heap.empty():
        
        cur_start, cur_end = min_heap.get()
        #1200,     1230
        
        while True:
            
            if min_heap.empty():
                break
            
            nxt_start, nxt_end = min_heap.queue[0]
            #1215,     1245
            
            if nxt_start <= cur_end:
                
                nxt_start, nxt_end = min_heap.get()
                
                #cur_start = min(cur_start, nxt_start)
                cur_end = max(cur_end, nxt_end)
            else:
                
                break
            
        if cur_start > prev_end:
            
            res.append([prev_end, cur_start])
            
        prev_end = cur_end
        
    return res
            
    
print(findAvailableTime(schedules1))        
print(findAvailableTime(schedules2))





from collections import defaultdict
from pprint import pprint as pp
from collections import Counter

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    photos = S.split('\n')
    
    d = defaultdict(str)
    l = []
    
    for photo in photos:
        
        seg = photo.split(', ')
        #print(seg)
        t = (seg[1], seg[2], seg[0])
        #d[t] = ''
        l.append(t)
    
    l.sort()
    
    
    city_count = Counter([k[0] for k in l])
    print(city_count)
    # d = sorted(d.items())
    # print(d)
    count = 1
    city = ''
    
    for key in l:
        
        if key[0] == city:
            count += 1
            print('*'+city)
        else:
            count = 1
            city = key[0]
            print(city)
        
        extension = key[2].split('.')[1]
        name = city+str(count).zfill(len(str(city_count[city])))+'.'+extension
        d[key] = name
    
    res = []

    for photo in photos:
        
        seg = photo.split(', ')
        t = (seg[1], seg[2], seg[0])
        res.append(d[t]) 
        
    #print(res)
    

solution('photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11')
    
    
'''  
    

1. create groups by city
2. Sort groups by city and time


count: {
    
}

{
    (Warsaw, 2013-09-05 14:07:13, myFriends.png) -> newfilename1
    (Warsaw, 2013-09-05 14:08:15, photo.jpg) -> newfilename2
}



city, time, photoname

', '.join(photoname, city, time)

photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11
'''
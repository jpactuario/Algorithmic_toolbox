# Uses python2

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    while len(segments) > 0:
        # find the smallest end point
        smallPoint = segments[0].end 
        smallIndex = 0
        for i in range(len(segments)):
            if segments[i].end < smallPoint:
                smallPoint = segments[i].end
                smallIndex = i
        points.append(segments[smallIndex].end)
        segments2 = []
        for s in segments:
            if  not(s.start <= smallPoint and smallPoint <=  s.end):
                segments2.append(s)
        segments = segments2
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    temp = map(int, input.split())
    n = temp[0]
    data = temp[1:]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print len(points)
    for p in points:
        print p,



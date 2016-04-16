#python2

# Intuition:
# start position is independent from end position
# Imagine Venn's diagram where the first circle represents segments where start position <= point (A)
# and the second circle represents where end position >= point (B)
# The number of segments satisfying both start position <= point and end position <= point is
# A + B - N
def fast_count_segments(starts, ends, points):
    cnt = [0]*len(points)
    starts.sort()
    ends.sort()
    for i in range(len(points)):
        if starts[0] > points[i]:
            A = 0
        elif starts[-1] <=  points[i]:
            A = len(starts)
        else:
            A = binary_search1(starts,points[i],0,len(starts))+1
        if ends[-1] < points[i]:
            B = 0
        elif ends[0] >= points[i]:
            B = len(ends)
        else:
            B = len(ends)-binary_search2(ends,points[i],0,len(ends))
        cnt[i] = A + B - len(starts)
    return cnt

def binary_search1(a, p, left, right):
    # Find rightmost point that is equal or less than p
    if left > right:
        return left - 1
    mid = (right + left) // 2
    if a[mid] < p:
        return binary_search1(a,p,mid+1,right)
    elif a[mid] > p:
        return binary_search1(a,p,left,mid-1)
    else:
        while mid < len(a) - 1:
            if a[mid+1]>p: return mid
            else: mid +=1
        return mid

def binary_search2(a, p, left, right):
    # Find leftmost point that is equal or greater than p
    if left > right:
        return left
    mid = (right + left) // 2
    if a[mid] > p:
        return binary_search2(a,p,left,mid-1)
    elif a[mid] < p:
        return binary_search2(a,p,mid+1,right)
    else:
        while mid > 0:
            if a[mid-1]<p: return mid
            else: mid -=1
        return mid

import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print x,

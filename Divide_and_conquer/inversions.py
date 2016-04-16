#python2

def get_number_of_inversions(a, count):
    if len(a) <= 1: return a, count
    mid = len(a) // 2
    b, count1 = get_number_of_inversions(a[:mid], count)
    c, count2 = get_number_of_inversions(a[mid:], count)
    # merging
    d, count = merge_count2(b, c, count1 + count2)
    return d, count

def merge_count(b, c, count):
    d = []
    while len(b) > 0 or len(c) > 0:
        if len(c) == 0:
            d.extend(b)
            break
        elif len(b) == 0:
            d.extend(c)
            break
        elif b[0] <= c[0]:
            d.append(b[0])
            b = b[1:]
        else:
            d.append(c[0])
            c = c[1:]
            count += len(b)
    return d, count

def merge_count2(b, c, count):
    d = [0]*(len(b)+len(c))
    j = 0 # counter for b
    k = 0 # counter for c
    for i in xrange(len(d)):
        if k >= len(c):
            d[i] = b[j]
            j += 1
        elif j >= len(b):
            d[i] = c[k]
            k += 1
        elif b[j] <= c[k]:
            d[i] = b[j]
            j += 1
        else:
            d[i] = c[k]
            k += 1
            count += len(b) - j
    return d, count

import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, a = data[0], data[1:]
    print get_number_of_inversions(a, 0)[1]

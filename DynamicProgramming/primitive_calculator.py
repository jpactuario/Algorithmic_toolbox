# python2

def optimal_sequence(n):
    sequence = [n]
    value = [0] * n  #value[0] is for n = 1, value[n-1] is for n = n 
    if n == 1: return sequence
    for i in range(1,n):
        a = value[i-1]
        if (i+1) % 2 == 0:
            b = value[(i+1)/2-1]
        else:
            b = 99999999
        if (i+1) % 3 == 0:
            c = value[(i+1)/3-1]
        else:
            c = 99999999
        value[i] = min(a,b,c) + 1
    # At this point, value[n-1] is the solution to the length of sequence.
    # Find Sequence.
    i = n
    while i > 1:
        if value[i-2] == value[i-1] - 1:
            sequence.append(i-1)
            i -= 1
        elif i % 3 == 0:
            if value[i/3 - 1] == value[i-1] - 1:
                sequence.append(i/3)
                i = i/3
        elif i % 2 == 0:
            if value[i/2 - 1] == value[i-1] - 1:
                sequence.append(i/2)
                i = i/2
    return sequence[::-1]

import sys
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print (len(sequence) - 1)
for x in sequence:
    print x,

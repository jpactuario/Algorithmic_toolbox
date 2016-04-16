# Uses python2

def match_pattern(P):
    for x in range(len(P)):
        if P[x][0] == P[x][1]:
            return P[x][0]
    return []

def find_pattern(n, m):
    F = [0,1] # Finonacci mod m series
    P = []    # Storing pattern
    i = 2
    J = 0     # Number of potential patterns available

    # Testing Pattern Recognition.
    # Seq = [0,1,1,1,1,0,1,0,1,1,1,1,0,1]

    while i <= n:
        # Generating Fibonacci sequence

        curr = (F[i-2]+F[i-1]) % m
        prev = F[i - 1]

        # Code for testing pattern recognition on arbitrary sequence -- satisfactory
        #curr = Seq[i]
        #prev = Seq[i-1]

        F.append(curr)

        if curr == 1 and prev == 0:
            J += 1
            P.append([F[:i-1],[F[i-1]]])
        for j in range(J):
            P[j][1].append(curr)
        if J > 0:
            pattern = match_pattern(P)
            if pattern != []:
                return pattern
        i += 1
    return F  # No pattern found.

def get_fibonaccihuge(n, m):
    if n <= 1:
        return n % m
    patt = find_pattern(n, m)
    return patt[n % len(patt)]


import sys

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))

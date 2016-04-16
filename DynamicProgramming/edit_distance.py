#python2
def edit_distance(s, t):
    m = len(s)
    n = len(t)
    D = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        D[i][0] = i
    for i in range(n+1):
        D[0][i] = i
    for i in range(1,m+1):
        for j in range(1,n+1):
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            match  = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                D[i][j] = min(insert, delete, match)
            else:
                D[i][j] = min(insert, delete, mismatch)
    return D[m][n]

if __name__ == "__main__":
    print(edit_distance(raw_input(), raw_input()))

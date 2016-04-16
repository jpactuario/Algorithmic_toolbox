# Uses python2

def calc_fib(n):
    if (n <= 1):
        return n
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2,n+1):
           arr[i] = arr[i-1]+arr[i-2] 
    return arr[n]
n = int(raw_input())
print(calc_fib(n))

# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)

# n = int(input())
# print(calc_fib(n))

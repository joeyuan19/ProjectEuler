
def palindrome(n):
    return str(n) == str(n)[::-1]


def solve():
    N = 50
    a = 0
    for i in range(99,10000):
        n = i
        c = 0
        while c < N:
            c += 1
            #print n
            #print int(str(n)[::-1])
            n += int(str(n)[::-1])
            #print n
            if palindrome(n):
                break
        if c == N:
            a += 1
                

    return a

from timer import time_function
print(time_function(solve))

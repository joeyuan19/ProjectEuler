"""
Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

"""

correct = {
    2:1,
    3:2,
    4:4,
    5:6,
    6:10,
    7:14,
}


def count(N):
    sol = [1]+[0]*(N)
    for i in range(1,N):
        for j in range(i,N+1):
            sol[j] += sol[j - i]
    return sol[-1]
            
count(100)


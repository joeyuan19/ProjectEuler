import itertools


def gen_sums(n,lim):
    for a in range(1,lim+1):
        for b in range(a+1,lim+1):
            c = n-(a+b)
            if c > 1 and lim+1 > c > max(a,b) and sum((a,b,c)) == n:
                yield [a,b,c]

def rev(li):
    return sorted(li)[::-1]

def _set(li):
    tmp = []
    for i in li:
        if i not in tmp:
            tmp.append(i)
    return tmp

#
#
#          1
#          |
#      0-6-7 2
#       /  |/
#      5   8
#     / \ /
#    4   9 
#         \
#          3
#
#
#
#
#

# forgot to add code to get answer, so copy-pasted in
sets = ((0,6,7),(1,7,8),(2,8,9),(3,9,5),(4,5,6))
a = [(1, 2, 3, 4, 5, 6, 8, 10, 7, 9), (1, 3, 5, 7, 9, 2, 6, 10, 4, 8), (1, 5, 4, 3, 2, 7, 10, 8, 6, 9), (1, 9, 7, 5, 3, 4, 10, 6, 2, 8), (2, 1, 5, 4, 3, 9, 7, 10, 8, 6), (2, 3, 4, 5, 1, 8, 10, 7, 9, 6), (2, 4, 6, 8, 10, 1, 5, 9, 3, 7), (2, 5, 3, 6, 9, 1, 7, 8, 4, 10), (2, 5, 8, 6, 9, 3, 4, 10, 1, 7), (2, 9, 6, 3, 5, 4, 8, 7, 1, 10), (2, 9, 6, 8, 5, 1, 10, 4, 3, 7), (2, 10, 8, 6, 4, 3, 9, 5, 1, 7), (3, 1, 9, 7, 5, 8, 4, 10, 6, 2), (3, 2, 1, 5, 4, 6, 9, 7, 10, 8), (3, 4, 5, 1, 2, 10, 7, 9, 6, 8), (3, 5, 2, 9, 6, 1, 10, 4, 8, 7), (3, 5, 7, 9, 1, 6, 10, 4, 8, 2), (3, 6, 9, 2, 5, 8, 4, 10, 1, 7), (4, 2, 10, 8, 6, 7, 3, 9, 5, 1), (4, 3, 2, 1, 5, 8, 6, 9, 7, 10), (4, 5, 1, 2, 3, 7, 9, 6, 8, 10), (4, 6, 8, 10, 2, 5, 9, 3, 7, 1), (5, 1, 2, 3, 4, 9, 6, 8, 10, 7), (5, 2, 9, 6, 3, 10, 4, 8, 7, 1), (5, 2, 9, 6, 8, 7, 1, 10, 4, 3), (5, 3, 1, 9, 7, 2, 8, 4, 10, 6), (5, 3, 6, 9, 2, 7, 8, 4, 10, 1), (5, 4, 3, 2, 1, 10, 8, 6, 9, 7), (5, 7, 9, 1, 3, 10, 4, 8, 2, 6), (5, 8, 6, 9, 2, 4, 10, 1, 7, 3), (6, 3, 5, 2, 9, 7, 1, 10, 4, 8), (6, 4, 2, 10, 8, 1, 7, 3, 9, 5), (6, 7, 8, 9, 10, 1, 3, 5, 2, 4), (6, 8, 5, 2, 9, 4, 3, 7, 1, 10), (6, 8, 10, 2, 4, 9, 3, 7, 1, 5), (6, 9, 2, 5, 3, 4, 10, 1, 7, 8), (6, 9, 2, 5, 8, 1, 7, 3, 4, 10), (6, 10, 9, 8, 7, 2, 5, 3, 1, 4), (7, 5, 3, 1, 9, 6, 2, 8, 4, 10), (7, 6, 10, 9, 8, 4, 2, 5, 3, 1), (7, 8, 9, 10, 6, 3, 5, 2, 4, 1), (7, 9, 1, 3, 5, 4, 8, 2, 6, 10), (8, 5, 2, 9, 6, 3, 7, 1, 10, 4), (8, 6, 4, 2, 10, 5, 1, 7, 3, 9), (8, 6, 9, 2, 5, 10, 1, 7, 3, 4), (8, 7, 6, 10, 9, 1, 4, 2, 5, 3), (8, 9, 10, 6, 7, 5, 2, 4, 1, 3), (8, 10, 2, 4, 6, 3, 7, 1, 5, 9), (9, 1, 3, 5, 7, 8, 2, 6, 10, 4), (9, 2, 5, 3, 6, 10, 1, 7, 8, 4), (9, 2, 5, 8, 6, 7, 3, 4, 10, 1), (9, 6, 3, 5, 2, 8, 7, 1, 10, 4), (9, 6, 8, 5, 2, 10, 4, 3, 7, 1), (9, 7, 5, 3, 1, 10, 6, 2, 8, 4), (9, 8, 7, 6, 10, 3, 1, 4, 2, 5), (9, 10, 6, 7, 8, 2, 4, 1, 3, 5), (10, 2, 4, 6, 8, 7, 1, 5, 9, 3), (10, 6, 7, 8, 9, 4, 1, 3, 5, 2), (10, 8, 6, 4, 2, 9, 5, 1, 7, 3), (10, 9, 8, 7, 6, 5, 3, 1, 4, 2)]

solutions = []
for solution in a:
    solution = [[solution[i] for i in s] for s in sets]
    solution = solution[solution.index(min(solution)):]+solution[:solution.index(min(solution))]
    solutions.append((solution,int(''.join(''.join(str(j) for j in i) for i in solution))))

solutions = [i for i in solutions if len(str(i[1])) == 16]
print max(solutions)

import sys
sys.exit()

class Skip(Exception):
    pass

sets = ((0,6,7),(1,7,8),(2,8,9),(3,9,5),(4,5,6))
solutions = []


for solution in itertools.permutations([i for i in range(1,11)]):
    print solution
    _last = -1
    try:
        for s in sets:
            _sum = sum(solution[i] for i in s)
            if _last < 0:
                print _sum
                _last = _sum
            if _sum != _last:
                raise Skip()
        solutions.append(solution)
    except Skip:
        print "skip"
        continue
    except KeyboardInterrupt:
        break
print solutions
    

import sys
sys.exit()




def solve(n,arm,digit_lim):
    sols = [sol for sol in gen_sums(n,digit_lim)]
    solutions = []
    for sol in itertools.permutations(sols,arm):
        for sol_a in itertools.permutations(sol[0]):
            for sol_b in itertools.permutations(sol[1]):
                if sol_a[2] == sol_b[1]:
                    for sol_c in itertools.permutations(sol[2]):
                        if sol_b[2] == sol_c[1]:
                            for sol_d in itertools.permutations(sol[3]):
                                if sol_c[2] == sol_d[1]:
                                    for sol_e in itertools.permutations(sol[4]):
                                        if sol_a[2] == sol_e[1]:
                                            solution = [sol_a,sol_b,sol_c,sol_d,sol_e]
                                            print '\t',solution
                                            solution = solution[solution.index(min(solution)):]+solution[:solution.index(min(solution))]
                                            print '\t',solution
                                            solutions.append(int(''.join(''.join(str(j) for j in i) for i in solution)))
    return set(solutions)

m = []

for i in range(1,100):
    print i 
    for j in solve(i,5,10):
        print i,j,len(str(j))
        if len(str(j)) == 16:
            m.append(j)
    print

print max(m)

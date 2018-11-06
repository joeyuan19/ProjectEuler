from timer import time_function
import sys
import matplotlib.pyplot as plt

# idea is to add the origin into the polygon and integrate with/without, if area increases

#                        y2  .
#   y1 .                     |
#      |                     |
#------------------------------------
#      x1                    x2
# I = int(x1,x2) y(x) dx
# I = int(...) mx+b
# I = m(x^2)/2 + bx|x=x1/x2
# I = (m/2)*(x2^2 - x1^2) + (y2-m*x2)*(x2-x1)
# I = ((y2-y1)/(x2-x1)/2)*(x2^2 - x1^2) + (y2-(y2-y1)/(x2-x1)*x2)*(x2-x1)

def integrate_polygon(p):
    l = len(p)
    _p = p + [p[0]]
    I = 0
    for i in range(l):
        p1 = _p[i]
        p2 = _p[i+1]
        dx = p2[0]-p1[0]
        if dx == 0:
            continue
        dy = p2[1]-p1[1]
        m = dy/dx
        I += m*(p2[0]**2 - p1[0]**2)/2 + (p2[1] - m*p2[0])*dx
    return abs(I)

A = (-340,495)
B = (-153,-910)
C = (835,-947)

X = (-175,41)
Y = (-421,-714)
Z = (574,-645)

def raytrace(p):
    l = len(p)
    _p = p + [p[0]]
    crossing = 0
    for i in range(l):
        p1 = _p[i]
        p2 = _p[i+1]
        if p2[1] >= 0 >= p1[1] or p2[1] <= 0 <= p1[1]:
            dx = p2[0]-p1[0]
            if dx == 0:
                if p2[0] >= 0:
                    crossing += 1
                continue
            dy = p2[1]-p1[1]
            m = dy/dx
            b = p1[1] - m*p1[0]
            if -b/m >= 0:
                crossing += 1
    return crossing%2 == 1 

def contains_origin(p):
    return integrate_polygon(p) > integrate_polygon([(0,0)]+p)
    
def plot_polygon(p):
    x = [i[0] for i in p] + [p[0][0]]
    y = [i[1] for i in p] + [p[0][1]]
    plt.plot(x,y)

def solve():
    with open('../files/p102_triangles.txt','r') as f:
        tris = [tuple(map(float,line.split(','))) for line in f] 
    tris = [[(tri[2*i],tri[2*i+1]) for i in range(3)] for tri in tris]
    c = 0
    for tri in tris:
        if raytrace(tri):
            c += 1
    return c

print(time_function(solve))



def is90(l1,l2):
    return sum(i*j for i,j in zip(l1,l2)) == 0

def line(p1,p2):
    return (p1[0]-p2[0],p1[1]-p2[1])

def is_right_tri(p1,p2,p3):
    if p1 == p2 or p2 == p3 or p1 == p3:
        return False
    l1 = line(p1,p2)
    l2 = line(p2,p3)
    l3 = line(p3,p1)
    lines = (l1,l2,l3)
    for i in range(len(lines)):
        if is90(lines[i],lines[(i+1)%len(lines)]):
            return True            
    return False

lim = 50+1
n = 0
for x1 in range(lim):
    for y1 in range(lim):
        for x2 in range(lim):
            for y2 in range(lim):
                print x1,y1,x2,y2
                if is_right_tri((0,0),(x1,y1),(x2,y2)):
                    n += 1

print n/2




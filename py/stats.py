with open('times.csv','r') as f:
    times = {}
    i = 1
    for line in f:
        try:
            times[i] = float(line)
        except:
            times[i] = None
        i += 1
print('Total Time:',sum(i for i in times.values() if i is not None))
print('Total <1min:',sum(i for i in times.values() if i is not None and i < 60))
print('Average <1min:',sum(i for i in times.values() if i is not None and i < 60)/len(list(i for i in times.values() if i is not None and i <60)))

first = True 
mi,mt = 0,0
for i,t in times.items():
    if first and t is not None and t >= 60:
        fi = i
        ft = t
        first = False
    if t is not None and t > mt:
        mt = t
        mi = i+1
print('first over 60:',fi)
print('first over 60 time:',ft)
print('Max time:',mt)
print('Max #:',mi)
l_gt_min = len(list(i for i in times.values() if i is not None and i >=60))
print('# of problems >1min:',l_gt_min)
solved = len(list(i for i in times.values() if i is not None))
print('# solved:',solved)
print('% solved:',round(l_gt_min/solved*100,2),"%")

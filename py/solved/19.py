#!/bin/sh

# P19.sh
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


#jan = 31
#feb = 28
#mar =31
#apr = 30 
#may = 31
#june = 30
#july = 31
#aug = 31
#sept = 30
#oct = 31
#nov = 30
#dec = 31

#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.

#m = 1
#3t = 2
#3w = 3
#3r = 4
#3f = 5
#3sat = 6
#3sun = 7

#while loop each year:
def sun(d,s):
    if d%7 == 0:
        s = s + 1
    return s
def year(d,s,m,y):
    for c in m:
        s = sun(d,s)
        if c == [28,29]:
            if y%4 == 0:
                d = d + c[1]
            else:
                d = d + c[0]
        else:
            d = d + c
    return d,s
    
    
    
months = [31,[28,29],31,39,31,39,31,31,39,31,39,31]
d = 1
s = 0
for i in range(1901,2001):
    d, s = year(d,s,months,i)

print d, s
        
    

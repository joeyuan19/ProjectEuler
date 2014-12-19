#!/bin/sh

# P31.py
# ProjectEuler
#
# Created by joe yuan on 4/11/11.
# Copyright 2011 Classified. All rights reserved.



count = 0
for a in range(2):
    if a*200 > 200:
        break
    for b in range(3):
        if a*200+b*100 > 200:
            break
        for c in range(5):
            if a*200+b*100+c*50 > 200:
                break
            for d in range(11):
                if a*200+b*100+c*50+d*20 > 200:
                    break
                for e in range(21):
                    if a*200+b*100+c*50+d*20+e*10 > 200:
                        break
                    for f in range(41):
                        if a*200+b*100+c*50+d*20+e*10+f*5 > 200:
                            break
                        for g in range(101):
                            if a*200+b*100+c*50+d*20+e*10+f*5+g*2 > 200:
                                break
                            for h in range(201):
                                sum = a*200+b*100+c*50+d*20+e*10+f*5+g*2+h*1
                                print a, b, c ,d, e, f, g, h
                                if sum > 200:
                                    break
                                if sum == 200:
                                    count = count + 1
                                
                                    
print count
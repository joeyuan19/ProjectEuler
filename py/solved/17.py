#!/bin/sh

# P17.py
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

def dig(n):
    if n == 0:
        return ''
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'
    if n == 3:
        return 'three'
    if n == 4:
        return 'four'
    if n == 5:
        return 'five'
    if n == 6:
        return 'six'
    if n == 7:
        return 'seven'
    if n == 8:
        return 'eight'
    if n == 9:
        return 'nine'

def tens(n):
    a = n/10
    if a == 0:
        return ''
    elif a == 1:
        if n == 10:
            return 'ten'
        elif n == 11:
            return 'eleven'
        elif n == 12:
            return 'twelve'
        elif n == 13:
            return 'thirteen'
        elif n == 14:
            return 'fourteen'
        elif n == 15:
            return 'fifteen'
        elif n == 16:
            return 'sixteen'
        elif n == 17:
            return 'seventeen'
        elif n == 18:
            return 'eighteen'
        elif n == 19:
            return 'nineteen'
    elif a == 2:
        return 'twenty'
    elif a == 3:
        return 'thirty'
    elif a == 4:
        return 'forty'
    elif a == 5:
        return 'fifty'
    elif a == 6:
        return 'sixty'
    elif a == 7:
        return 'seventy'
    elif a == 8:
        return 'eighty'
    elif a == 9:
        return 'ninety'
    


def hundred(n,e):
    if e > 0:
        r = 'and'
    else:
        r = ''
    if n<10:
        return dig(n) + 'hundred' + r
    else:
        return dig(n/10) + 'thousand' + r



def namenumber(n):
    # names numbers using the form abc 
    # for intance 123
    # one hundred and twenty three
    # a = onehundredand
    # b = twenty
    # c = three
    if n > 99:
        a = hundred(n/100,n%100)
    else:
        a = ''
    if n >9:
        b = tens(n%100)
    else:
        b = ''
    if not 20 > n%100 > 10:
        c = dig(n%10)
    else:  
        c = ''
    return a+b+c
name = ''
for i in range(1,1001):
    print namenumber(i)
    name = name + namenumber(i)
print name
print len(name)
    
    
    
    
    
    
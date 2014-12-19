#!/bin/sh

# P59.py
# ProjectEuler
#
# Created by joe yuan on 9/12/11.
# Copyright 2011 Classified. All rights reserved.
import math
"""
data = map(int,open('cipher1.txt').read().split(","))

def repeat(l):
    while True:
        for i in l:
            yield i

l = map(ord,"abcdefghijklmnopqrstuvwxyz")
for a in l:
    for b in l:
        for c in l:
            dec=[foo^bar for foo,bar in zip(data,repeat((a,b,c)))]
            if any(ch<32 or ch>125 for ch in dec) or\
                ord("#") in dec:
                    continue
            print map(chr,(a,b,c))
            print "".join(map(chr,dec))




a = "(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father."
b = [ord(i) for i in a]
print sum(b)

"""




f = open("cipher1.TXT")
text = [i for i  in f]
code = []
for i in text:
    s = ''
    for c in i:
        if c == ',':
            code.append(int(s))
            s = ''
        else:
            s += c
    code.append(int(s))

f = [code.count(i) for i in range(257)]

    
key = 'god'

def key_change(x):
    #changes key not generally, just for this program
    # will just change to the next three lowercase letter key
    new_key = list(x)
    if ord(new_key[-3]) == ord('z'):
        if ord(new_key[-2]) == ord('z'):
            if ord(new_key[-1]) == ord('z'):
                print "uh oh"
                return new_key
                
    if ord(new_key[-1]) < ord('z'):
        new_key[-1] = chr(ord(new_key[-1])+1)
    elif ord(new_key[-2]) < ord('z'):
        new_key[-1] = 'a'
        new_key[-2] = chr(ord(new_key[-2])+1)
    elif ord(new_key[-3]) < ord('z'):
        new_key[-1] = 'a'
        new_key[-2] = 'a'
        new_key[-3] = chr(ord(new_key[-3])+1)
    new_key = ''.join(i for i in new_key)
    return new_key

def filter(s):
    if x < 32 or x > 122:
        return False
    if x > 34 and x < 39:
        return False
    if x == ord('/'):
        return False
    if x == 64:
        return False
    if x > 90 and x < 97:
        return False
    return 1 

def XOR(code,key,solve=True):
    s = ''
    for i in range(len(code)):
        
    return ''.join(chr(ord(key[i%len(key)])-code[i]) for i in range(len(code)) if check(i))
# print code

for i in range(len(code)):
    print key[i%len(key)], code[i], chr( ord(key[i%len(key)])-code[i] )

print XOR(code,'gos')


 
for i in range(26**3):
    c = XOR(code,key)
    print key
    print c
    print '\n\n'
    key = key_change(key)
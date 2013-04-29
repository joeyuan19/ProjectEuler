#!/bin/sh

# P5_theory.sh
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


#!/bin/sh

# P5.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

JUST IN PLAIN TEXT WHOOOOO


so the number has to be divisible by 
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
doing a prime factorization:
you can eliminate certain numbers if you know something say 
is divisible by 12 then you know it is also devisible by 2,3,and 4
so start big!
20 - 20,10,5,4,2,1
[6,7,8,9,11,12,13,14,15,16,17,18,19,20]
19 - 19,1
[6,7,8,9,11,12,13,14,15,16,17,18,19,20]
18 - 18,9,2,1
[6,7,8,11,12,13,14,15,16,17,18,19,20]
17 - 17,1
[6,7,8,11,12,13,14,15,16,17,18,19,20]
16 - 16,8,4,2,1
[6,7,11,12,13,14,15,16,17,18,19,20]
15 - 15,5,3,1
[6,7,11,12,13,14,15,16,17,18,19,20]
14 - 14,7,2,1
[6,11,12,13,14,15,16,17,18,19,20]
13 - 13,1
[6,11,12,13,14,15,16,17,18,19,20]
12 - 12,6,4,3,2,1
[11,12,13,14,15,16,17,18,19,20]
11 - 11,1
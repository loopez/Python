#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Check if an integer is a perfect square ang give its square root.

ans= 0
neg_flag= False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag= True
while ans**2 < x:
        ans+=1
if ans**2 == x:
    print("Square root of " + str(x) + " is " + str(ans))
else:
    print( str(x) + ' is not a perfect square')
if neg_flag:
    print("Just checking... did you mean ", -x, '?')

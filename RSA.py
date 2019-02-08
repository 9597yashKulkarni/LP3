# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:35:02 2019

@author: yashk
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:54:47 2019

@author: yashk
"""
import random

def generateKey():
    p=random.randint(2,999)
    q=random.randint(2,999)
    #p=7
    #q=17
    N=0
    E=0
    D=0
    flag=isPrime(p)
    flag2=isPrime(q)
    if flag==0 and flag2==0:
        print("{} and {} is a prime number".format(p,q))
        #2nd step
        N=p*q
        
        #Finding E
        product=(p-1)*(q-1)        
        for i in range(1,99999):
            if (product%i!=0):
                E=i                
                break
        #Finding D
        for i in range(1,99):
            if(((i*E)%product)==1):
                D=i
            else:
               # generateKey()
                break
        print("{} is N".format(N)) 
        print("{} is product".format(product))
        print("{} is E".format(E))
        print("{} is D".format(D))
    else:
        generateKey()

def isPrime(num):
    flag=0
    r=int(num/2)
    for i in range(2,r):
        if(num%i==0):
            flag=1
            break
        i=i+1

    return flag

generateKey()

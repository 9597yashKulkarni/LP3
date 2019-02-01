# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:54:47 2019

@author: yashk
"""
import random

def generateKey():
    num1=random.randint(2,9999)
    num2=random.randint(2,9999)
    flag=isPrime(num1)
    flag2=isPrime(num2)
    if flag==0 and flag2==0:
        print("{} and {} is a prime number".format(num1,num2))
        x=random.randint(0,9999)
        print("x is {}".format(x))
        y=random.randint(0,9999)
        print("y is {}".format(y))
        A=(num2**x)%num1
        print("A is (num2^x)mod num1 = {}".format(A)) 
        B=(num2**y)%num1
        print("B is (num2^y)mod num1 = {}".format(B))
        key1=(B**x)%num1
        key2=(A**y)%num1
        print("Key1 is {}".format(key1))
        print("Key2 is {}".format(key2))
        return num1,num2
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

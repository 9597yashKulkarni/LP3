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
    
    flag=isPrime(p)
    flag2=isPrime(q)
    if flag==0 and flag2==0:
        RSA(p,q)

    else:
        generateKey()

def RSA(p,q):
    print("{} and {} are prime numbers".format(p,q))
    #2nd step
    N=p*q
    
    #Finding E
    product=(p-1)*(q-1)        
    for i in range(1,99999):
        if (product%i!=0):
            E=i                
            break
    #Finding D
    for i in range(1,product-1):
        if(((i*E)%product)==1):
            D=i
            break
        
    #print("N  is {}".format(N)) 
    #print("product((p-1)*(q-1)) is {}".format(product))
    print("Encryption key is {}".format(E))
    print("Decryption key is {}".format(D))
    
    """
    PT=input("Enter any plain text")
    #PT=PT.split()
    print("PT is "+PT)
    #A =0
    PT1=ord(PT)-65
    CT1=(PT1**E)%N
    print("CT is {}".format(CT1))
    
    PT2=(CT1**D)%N
    print("PT2 is {}".format(PT2))
    PT2=PT2+65
    PT2=chr(PT2)
    print("PT received is "+PT2)
"""
    PT=[]
    pt=[]
    ct=[]
    CT=[]
    PT=input("Enter any text \n")
    for i in PT:
        #print(i)
        pt.append(ord(i))#removing -65
    print("Plain text is "+PT)
    
    for i in pt:
        ct.append((i**E)%N)
    
    print("cipher text in numbers is {}".format(ct))
    for i in ct:
        CT.append(chr(((i**D)%N)))#removing +65
        
    
    print("Cipher text is :'",end="")
    for i in CT:
        print(i,end="")
    print("'")
def isPrime(7):
    flag=0
    r=int(num/2)
    for i in range(2,r):
        if(num%i==0):
            flag=1
            break
        #i=i+1

    return flag

N=0
E=0
D=0
generateKey()

"""
OUTPUT:
337 and 433 are prime numbers
Encryption key is 5
Decryption key is 58061

Enter any text 
Yash Kulkarni
Plain text is Yash Kulkarni
cipher text in numbers is [100542, 35328, 113077, 73807, 138523, 79573, 141949, 57515, 28550, 35328, 15795, 91072, 127202]
Cipher text is :'Yash Kulkarni'
"""
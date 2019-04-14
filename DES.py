# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:54:54 2019

@author: yashk
"""

import numpy as np
planeText=input('Enter any text\n')
bitText=[]
bt=[]
ptInBin=[]

get_bin = lambda x, n: format(x, 'b').zfill(n)

for i in planeText:
    bitText.append(ord(i))
    
print(bitText)


for i in bitText:
    bt.append(get_bin(i,8))
   
    
print(bt) 

for i in bt:
    for bit in i:
        ptInBin.append(int(bit))


print(ptInBin)


bt64blk=ptInBin[:64]
del(ptInBin[:64])   #deleting the converted 
print(bt64blk)

piblk=[]
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

for i in PI:
    piblk.append(bt64blk[i-1])
    
print(piblk)

LPT=piblk[:32]
RPT=piblk[32:]

print("LPT is :")
print(LPT)
print()

print("RPT is :")
print(RPT)
#print(bin(105))
#print(int('1101001',2))
print()


for round in range(0,16):
        
    print("Round {} Begins ".format(round))
    RPT1=RPT[0:4]
    RPT2=RPT[4:8]
    RPT3=RPT[8:12]
    RPT4=RPT[12:16]
    RPT5=RPT[16:20]
    RPT6=RPT[20:24]
    RPT7=RPT[24:28]
    RPT8=RPT[28:32]
    
    RPT1.insert(0,RPT[31])
    RPT1.append(RPT[4])
    
    RPT2.insert(0,RPT[3])
    RPT2.append(RPT[8])
    
    RPT3.insert(0,RPT[7])
    RPT3.append(RPT[12])
    
    RPT4.insert(0,RPT[11])
    RPT4.append(RPT[16])
    
    RPT5.insert(0,RPT[15])
    RPT5.append(RPT[20])
    
    RPT6.insert(0,RPT[19])
    RPT6.append(RPT[24])
    
    RPT7.insert(0,RPT[23])
    RPT7.append(RPT[28])
    
    RPT8.insert(0,RPT[27])
    RPT8.append(RPT[0])
    
    RPT48=RPT1+RPT2+RPT3+RPT4+RPT5+RPT6+RPT7+RPT8
    #print(RPT48)
    
    #RPT48=np.array(RPT48)
    
    key=[]
    import random
    for i in range(48):
        key.append(random.randint(0,1))
    #print(key)
    #key=np.array(key)    
    
    XORED=np.array(RPT48)^np.array(key)
    #print("after xor")
    #print(XORED)
    """
    XORED1=XORED[0:6]
    XORED2=XORED[6:12]
    XORED3=XORED[12:18]
    XORED4=XORED[18:24]
    XORED5=XORED[24:30]
    XORED6=XORED[30:36]
    XORED7=XORED[36:42]
    XORED8=XORED[42:48]
    
    print(XORED1)
    rowId=str(XORED1[0])+str(XORED1[5])
    colId=str(XORED1[1:5])
    print(colId)
    print(rowId)
    """
    
    #SBOX
    S_BOX = [
             
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],  
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ], 
    
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ], 
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
       
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
    ]
    
    AfterSBox=[]
    AfterSBox8=[]
    for i in range(8):
        temp=XORED[(6*i):((i+1)*6)]
        rowId=str(temp[0])+str(XORED[5])
        rowId=int(rowId,2)
        colId=str(temp[1])+str(temp[2])+str(temp[3])+str(temp[4])
        colId=int(colId,2)
        AfterSBox8.append(get_bin(S_BOX[i][rowId][colId],4))
    #print(AfterSBox8)
    
    for nibble in AfterSBox8:
        for bit in nibble:
            AfterSBox.append(int(bit))
            
    #print(AfterSBox)
    
    #Permut made after each SBox substitution for each round
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    
    pBox=[]
    for i in P:
        pBox.append(AfterSBox[i-1])
        
        
    #print(pBox)
    
    LastXored=np.array(pBox)^np.array(LPT)
    LastXored=list(LastXored)
    #print(LastXored)
    
    LPT=RPT
    RPT=LastXored
    
    print("After Round {} LPT:\n{} \nRPT\n{}".format(round,LPT,RPT))
    
    
forFinalPermutation=LPT+RPT

ciphertext=[]
#Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

for i in PI_1:
    ciphertext.append(forFinalPermutation[i-1])
    
print("ciphertext is :\n{}".format(ciphertext))
"""
#Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]



OUTPUT:
Enter any text
Yash Kulkarni

ciphertext is :
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
"""
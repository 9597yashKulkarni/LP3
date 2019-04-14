# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:12:37 2019

@author: yashk
"""
"""
from Crypto.Cipher import DES
import base64
import os

import random
key= b'azxswedf'
for i in range(0,64):
    key.append(i)
key=str(key)
key=key[0:7]

cipher=DES.new(key,DES.MODE_OFB)
pltxt=b'Yash Kulkarni'
msg=cipher.iv+cipher.encrypt(pltxt)
print(msg)
"""

from Crypto.Cipher import DES3
from Crypto import Random
key = b'Sixteen byte key 1234567'
iv = Random.new().read(DES3.block_size)
cipher = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = b' Yash Prashant Kulkarni 12345678'
msg = iv + cipher.encrypt(plaintext)

print(msg)

"""
OUTPUT:
b'\x95\rz\x93\xba\xec&\xae\x90\x07c\x90\xc2I;I\x0b*\x04\x04\x8f\xb5\x16\xea\xbf?\xf4r
\xd4\x06hM\x83\xb9\x10\xc5@8\x11)'

"""


from Crypto.Cipher import AES
from Crypto import Random
key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')

print(msg)

ct=cipher.decrypt(msg)
print(ct)

"""
OUTPUT:
Encryption:
b'\x9e\xa7\xb0\x10\xce\xee\xcb\xdc\xc5\x9e\x1d\xccC\x8d\x98>i\xdcM\'\x08L\xa7"\x10 \x02{\xfb\xd1'

Decryption:
b"6\x81\xdc\x8e\xe9\x01\xa9\xb1'\xbd\x11H\x1e\xbe\x8a\x1fAttack at dawn"
"""
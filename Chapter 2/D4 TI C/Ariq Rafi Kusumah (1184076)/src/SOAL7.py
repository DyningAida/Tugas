# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:13:22 2019

@author: Asus
"""

i=0 
npm=input("Masukkan NPM : ") 
while i <1: 
    if len(npm) <7 : 
        print("NPM kurang dari 7 digit masukkan kembali NPM Anda ! ") 
        npm=input("masukkan NPM : ") 
    elif len(npm) >7 : 
        print("NPM lebih dari 7 digit masukkan kembali NPM Anda ! ") 
        npm=input("masukkan NPM : ") 
    else : 
        i=1 
a=npm[0] 
b=npm[1] 
c=npm[2] 
d=npm[3] 
e=npm[4] 
f=npm[5] 
g=npm[6] 
y=1
for x in a ,b, c ,d, e , f , g : 
    y*=int(x)
print (y) 
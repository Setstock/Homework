#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:37:40 2022

@author: patcharee
"""

import random
N = int(input("How many stick in the pile? : "))
print("There are",N,"sticks in the pile.")
name = str(input("What is your name? : "))
i=0
while (N != 0):
    if (i%2 == 0):
        x = int(input(str(name)+" , How many stick you will take? (1 or 2 ) : "))
        if (x>2):
            print("No you can't take more than 2 sticks!")
        elif(x<1):
            print("No you can't take less than 1 stick!")
        elif(N-x < 0):
            print("there aren't enough sticks to take")
        else:
            N = N-x
            i += 1
            if(N == 0):
                print(name," take the last  stick.")
                print("Computer Winnnnn",name,"So saddd")
            elif(N):
                print("There are",N,"Sticks in the pile.\n")
    else:
        com = random.randint(1, 2)
        print("Conputer take : ",com)
        if(N - com < 0 ):
            print("There aren't enough sticks to take.")
        else:
            N=N-com
            i += 1
            if(N == 0):
                print("Computer take the last stick.")
                print(name,"Winnn Computer so sad")
            else:
                print("There are",N,"sticks in the pile.\n")
            
            
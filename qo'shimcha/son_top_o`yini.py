# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:44:26 2023

@author: Lenovo
"""
import random

def sontop(x=15):
    komputer = random.randint(1, x)
    print(f"Men 1 dan {x} gacha oraliqdan bitta son o`yladim.\
 Siz uni topa olasizmi?")
    
    count = 0
    while True:
        count += 1
        user = int(input(">>> "))
        if user>komputer:
            print("Men o`ylagan son bundan kichik")
        elif user<komputer:
            print("Men o`ylagan son bundan katta")
        else:
            print("Javobingiz to`g`ri!")
            break
    print(f"Siz {count}ta taxmin bilan topdingiz!\n")
    return count    
    
def sontop_pc(x=15):
    input(f"Siz 1 dan {x} gacha bo`lgan sonlardan bitta son o`ylang.\
 Men uni topishga harakat qilaman!\n")
    quyi = 1
    yuqori = x
    count = 0
    while True:
        count += 1
        if quyi != yuqori:
            komputer = random.randint(quyi, yuqori)
        else:
            komputer = quyi
        
        user = input(f"Siz o`ylagan son {komputer}. Agar to`g`ri \
bo`lsa (t), undan katta bo`lsa (+) yoki kichik \
bo`lsa (-) belgisini yozing: ")
        if user == "+":
            quyi = komputer + 1
        elif user == "-":
            yuqori = komputer - 1
        else:
            print(f"{count} ta urunishda topdim!")
            break
    return count
    
def play(x=15):
    yana = True
    while yana:
        user = sontop(x)
        komputer = sontop_pc(x)
        if user>komputer:
            print(f"Men {komputer} ta taxmin bilan g`alaba qozondim!")
        elif user<komputer:
            print(f"Siz {user} ta taxmin bilan g`alaba qozondingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o`ynashni xohlaysizmi? (1 yoki 0) : "))
        
play(x=15)
        
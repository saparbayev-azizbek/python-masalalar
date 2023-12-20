# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:44:26 2023

@author: Lenovo
"""

def auta_info(kompaniya,nom,rang,yili,narxi):
    auto = {'kompaniya':kompaniya,
            'nom':nom,
            'rang':rang,
            'yili':yili,
            'narxi':narxi
        }
    return auto

def auto_input():
    autolar = []
    while True:
        kompaniya = input("Ishlab chiqaruvchi : "),
        nom = input("Nomi : "),
        rang = input("Rangi : "),
        yili = input("Yili : "),
        narxi = input("Narxi : ")
        autolar.append(auta_info(kompaniya, nom, rang, yili, narxi))
        javob = input("Yana kiritishni xohlaysizmi(yes/no) : ")
        if (javob == 'no'):
            break
    return autolar

def auto_print(kompaniya,nom,rang,yili,narxi):
    print(f"{rang.title()} {nom.title()}ning narxi {narxi}$")
    

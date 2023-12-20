# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:14:36 2023

@author: Lenovo
"""

import requests
try:
    oyat = 4
    url = f'https://api.alquran.cloud/v1/ayah/{oyat}/uz.sodik'
    res = requests.get(url)
    r = res.json()
    
    print(r['data']['text'])
except:
    print("Noto'g'ri oyat kiritdingiz!")
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:51:31 2023

@author: Lenovo
"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
y = car.get("model")
z = car.pop("year")
w = car.popitem()
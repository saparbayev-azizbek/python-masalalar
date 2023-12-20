# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:54:13 2023

@author: Lenovo
"""

import requests
from pprint import pprint
url = 'https://dailyprayer.abdulrcs.repl.co/api/tashkent'
pprint(requests.get(url).json()['today'])
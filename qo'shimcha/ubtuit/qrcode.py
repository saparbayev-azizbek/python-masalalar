# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 00:00:38 2023

@author: Lenovo
"""

import qrcode

def qr_code(data='https://www.youtube.com/watch?v=q6J-fawK1HE&list=PLG4WY0YXEBFvTuEVliNEWTiC3pwcQ4hYx&index=3'):
    filename = 'qr.png'
    image = qrcode.make(data)
    return image.save(filename)
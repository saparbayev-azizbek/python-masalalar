# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 18:05:15 2023

@author: Lenovo
"""

import unittest
from circle import getArea, getPerimeter
class CircleTest(unittest.TestCase):
    def test_getArea(self):
        value = getArea(5)
        self.assertEqual(value, 78.53975)
        
    def test_getPerimeter(self):
        value = getPerimeter(5)
        self.assertAlmostEqual(value, 31.4159,5)
        
unittest.main()
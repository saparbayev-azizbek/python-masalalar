# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:11:59 2023

@author: Lenovo
"""

def hex_to_binary(hex_num):
    hex_num = hex_num.upper()
    hex_to_bin_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    if len(hex_num) == 1:
        return hex_to_bin_dict[hex_num]

    return hex_to_binary(hex_num[:-1]) + hex_to_bin_dict[hex_num[-1]]

# Example usage
hex_num = "01"
binary_num = hex_to_binary(hex_num)
print(f"The binary representation of {hex_num} is: {binary_num}")


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:30:21 2023

@author: Lenovo
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_closest_key(root, target):
    closest_key = float('inf')  # Ancha katta qiymat bilan boshlaymiz
    closest_value = None

    while root is not None:
        if abs(root.value - target) < closest_key:
            closest_key = abs(root.value - target)
            closest_value = root.value

        if target < root.value:
            root = root.left
        else:
            root = root.right

    return closest_value

# Binar daraxtni tuzamiz
# Masalan:  10
#          /  \
#         5   15
#        / \
#       2   7
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

# Test qilamiz
target_value = 8
result = find_closest_key(root, target_value)
print(f"Berilgan binar daraxtda {target_value} ga eng yaqin bo'lgan tugun kaliti: {result}")

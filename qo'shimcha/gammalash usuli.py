# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:44:45 2023

@author: Lenovo
"""

from Crypto.PublicKey import ECC
from Crypto.Cipher import ECC_AES_GCM

def generate_key_pair():
    # Kalit so'z juftlikini generatsiya qilish
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()

    return private_key, public_key

def encrypt(message, public_key):
    # Shifrlash uchun kalitni olish
    cipher = ECC_AES_GCM.new(public_key)

    # Matnni shifrlash
    ciphertext = cipher.encrypt(message.encode())

    return ciphertext

def decrypt(ciphertext, private_key):
    # Deshifrlash uchun kalitni olish
    cipher = ECC_AES_GCM.new(private_key)

    # Shifrlangan matnni qaytarish
    decrypted_message = cipher.decrypt(ciphertext)

    return decrypted_message.decode()

# Kalit so'z juftlikini generatsiya qilish
private_key, public_key = generate_key_pair()

# Shifrlash va deshifrlash uchun matn
original_message = "Hello, World!"

# Matnni shifrlash
encrypted_message = encrypt(original_message, public_key)
print(f"Shifrlangan matn: {encrypted_message}")

# Shifrlangan matnni deshifrlash
decrypted_message = decrypt(encrypted_message, private_key)
print(f"Asl matn: {decrypted_message}")

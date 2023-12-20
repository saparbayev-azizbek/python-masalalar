"3.	Dekning juft elementlari yig„indisini hisoblang"

from collections import deque

def juft_elementlar_yigindisi(deque_obj):
    juft_yigindi = 0
    for element in deque_obj:
        if element % 2 == 0:
            juft_yigindi += element
    return juft_yigindi

# Deque yaratish
my_deque = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Juft elementlari yig'indisini hisoblash
result = juft_elementlar_yigindisi(my_deque)

# Natijani chop etish
print(f"Juft elementlar yig'indisi: {result}")

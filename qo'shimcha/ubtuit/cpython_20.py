def tub(x):
    m = True
    if x == 1:
        m = False
    elif x>0:
        for j in range(2,x+1):
            if x%j == 0:
                m = False
    return m

a = int(input())
s = 0
for i in range(1,a+1):
    if tub(i) == 1:
        s = s + i
print(s)